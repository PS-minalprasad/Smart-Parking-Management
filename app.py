from flask import Flask, jsonify, request
from parking_service import ParkingLotService


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        DATABASE_URL="parking.db",
        JSON_SORT_KEYS=False,
    )

    if test_config:
        app.config.update(test_config)

    service = ParkingLotService(app.config["DATABASE_URL"])

    @app.route("/")
    def index():
        return """
        <!doctype html>
        <html lang=\"en\">
        <head>
          <meta charset=\"utf-8\">
          <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
          <title>Smart Parking Management</title>
          <style>
            :root { color-scheme: dark; }
            body { font-family: Arial, sans-serif; margin: 0; background: #0f172a; color: #f8fafc; }
            .container { max-width: 980px; margin: 0 auto; padding: 32px 20px 60px; }
            .card { background: #111827; border: 1px solid #334155; border-radius: 16px; padding: 24px; box-shadow: 0 10px 30px rgba(0,0,0,.25); }
            h1 { margin-top: 0; }
            form { display: grid; gap: 12px; margin-top: 16px; }
            input, select, button { padding: 10px 12px; border-radius: 8px; border: 1px solid #475569; background: #020617; color: #f8fafc; }
            button { background: linear-gradient(135deg, #2563eb, #7c3aed); border: none; cursor: pointer; font-weight: 700; }
            .grid { display: grid; gap: 16px; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); margin-top: 24px; }
            .stat { background: #1e293b; padding: 16px; border-radius: 12px; }
            table { width: 100%; border-collapse: collapse; margin-top: 20px; }
            th, td { padding: 10px; border-bottom: 1px solid #334155; text-align: left; }
          </style>
        </head>
        <body>
          <div class=\"container\">
            <div class=\"card\">
              <h1>Smart Parking Management</h1>
              <form id=\"parking-form\">
                <input id=\"vehicle_no\" placeholder=\"Vehicle Number\" required>
                <input id=\"owner_name\" placeholder=\"Owner Name\" required>
                <select id=\"vehicle_type\">
                  <option value=\"car\">Car</option>
                  <option value=\"bike\">Bike</option>
                </select>
                <button type=\"submit\">Park Vehicle</button>
              </form>
              <div class=\"grid\">
                <div class=\"stat\"><strong>Total Vehicles</strong><div id=\"vehicle-count\">0</div></div>
                <div class=\"stat\"><strong>Total Collection</strong><div id=\"total-collection\">₹0</div></div>
              </div>
              <table>
                <thead><tr><th>Vehicle</th><th>Owner</th><th>Type</th><th>Fee</th></tr></thead>
                <tbody id=\"vehicle-list\"></tbody>
              </table>
            </div>
          </div>
          <script>
            async function refresh() {
              const vehicles = await fetch('/api/vehicles').then(r => r.json());
              const tbody = document.getElementById('vehicle-list');
              tbody.innerHTML = '';
              vehicles.forEach(v => {
                const row = document.createElement('tr');
                row.innerHTML = `<td>${v.vehicle_no}</td><td>${v.owner_name}</td><td>${v.vehicle_type}</td><td>₹${v.fee}</td>`;
                tbody.appendChild(row);
              });
              document.getElementById('vehicle-count').textContent = vehicles.length;
              const total = vehicles.reduce((sum, v) => sum + v.fee, 0);
              document.getElementById('total-collection').textContent = '₹' + total;
            }
            document.getElementById('parking-form').addEventListener('submit', async (event) => {
              event.preventDefault();
              const payload = {
                vehicle_no: document.getElementById('vehicle_no').value,
                owner_name: document.getElementById('owner_name').value,
                vehicle_type: document.getElementById('vehicle_type').value,
              };
              await fetch('/api/vehicles', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(payload)});
              event.target.reset();
              refresh();
            });
            refresh();
          </script>
        </body>
        </html>
        """

    @app.route("/api/vehicles", methods=["GET"])
    def list_vehicles():
        return jsonify(service.get_vehicles())

    @app.route("/api/vehicles", methods=["POST"])
    def create_vehicle():
        data = request.get_json(silent=True) or {}
        vehicle_no = (data.get("vehicle_no") or "").strip()
        owner_name = (data.get("owner_name") or "").strip()
        vehicle_type = (data.get("vehicle_type") or "car").strip().lower()

        if not vehicle_no or not owner_name:
            return jsonify({"error": "vehicle_no and owner_name are required"}), 400

        vehicle = service.park_vehicle(vehicle_no, owner_name, vehicle_type)
        return jsonify(vehicle), 201

    @app.route("/api/vehicles/<vehicle_no>", methods=["GET"])
    def get_vehicle(vehicle_no):
        vehicle = service.search_vehicle(vehicle_no)
        if not vehicle:
            return jsonify({"error": "vehicle not found"}), 404
        return jsonify(vehicle)

    @app.route("/api/vehicles/<vehicle_no>", methods=["DELETE"])
    def delete_vehicle(vehicle_no):
        deleted = service.remove_vehicle(vehicle_no)
        return jsonify({"deleted": deleted, "vehicle_no": vehicle_no})

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
