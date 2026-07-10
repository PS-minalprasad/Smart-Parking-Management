import sqlite3
from typing import List, Dict, Any


class ParkingLotService:
    def __init__(self, db_path: str = "parking.db"):
        self.db_path = db_path
        self.init_db()

    def init_db(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS vehicles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    vehicle_no TEXT NOT NULL UNIQUE,
                    owner_name TEXT NOT NULL,
                    vehicle_type TEXT NOT NULL,
                    fee INTEGER NOT NULL,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            conn.commit()

    def _get_fee(self, vehicle_type: str) -> int:
        return 100 if vehicle_type.lower() == "car" else 50

    def park_vehicle(self, vehicle_no: str, owner_name: str, vehicle_type: str) -> Dict[str, Any]:
        fee = self._get_fee(vehicle_type)
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "INSERT INTO vehicles (vehicle_no, owner_name, vehicle_type, fee) VALUES (?, ?, ?, ?)",
                (vehicle_no, owner_name, vehicle_type.lower(), fee),
            )
            conn.commit()
            vehicle_id = cursor.lastrowid

        return {
            "id": vehicle_id,
            "vehicle_no": vehicle_no,
            "owner_name": owner_name,
            "vehicle_type": vehicle_type.lower(),
            "fee": fee,
        }

    def get_vehicles(self) -> List[Dict[str, Any]]:
        with sqlite3.connect(self.db_path) as conn:
            rows = conn.execute(
                "SELECT id, vehicle_no, owner_name, vehicle_type, fee FROM vehicles ORDER BY id DESC"
            ).fetchall()

        return [
            {
                "id": row[0],
                "vehicle_no": row[1],
                "owner_name": row[2],
                "vehicle_type": row[3],
                "fee": row[4],
            }
            for row in rows
        ]

    def search_vehicle(self, vehicle_no: str) -> Dict[str, Any] | None:
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute(
                "SELECT id, vehicle_no, owner_name, vehicle_type, fee FROM vehicles WHERE vehicle_no = ?",
                (vehicle_no,),
            ).fetchone()

        if not row:
            return None

        return {
            "id": row[0],
            "vehicle_no": row[1],
            "owner_name": row[2],
            "vehicle_type": row[3],
            "fee": row[4],
        }

    def remove_vehicle(self, vehicle_no: str) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("DELETE FROM vehicles WHERE vehicle_no = ?", (vehicle_no,))
            conn.commit()

        return cursor.rowcount > 0

    def total_collection(self) -> int:
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute("SELECT COALESCE(SUM(fee), 0) FROM vehicles").fetchone()

        return int(row[0] or 0)
