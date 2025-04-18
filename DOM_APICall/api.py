from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

PER_PAGE = 10
API_BASE = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_evolution(species_url):
    """Lấy chuỗi tiến hóa của Pokémon từ API."""
    response = requests.get(species_url)
    species_data = response.json()

    # Lấy thông tin chuỗi tiến hóa
    evolution_url = species_data["evolution_chain"]["url"]
    evolution_data = requests.get(evolution_url).json()

    # Trả về danh sách các Pokémon trong chuỗi tiến hóa
    evolutions = []
    chain = evolution_data["chain"]
    while chain:
        evolutions.append({
            "name": chain["species"]["name"],
            "sprite": get_pokemon_sprite(chain["species"]["name"])
        })
        chain = chain["evolves_to"][0] if chain["evolves_to"] else None
    return evolutions

def get_pokemon_sprite(name):
    """Lấy ảnh của Pokémon từ API."""
    response = requests.get(f"{API_BASE}{name}")
    data = response.json()
    return data["sprites"]["front_default"]

@app.route("/")
def index():
    """Hiển thị danh sách Pokémon với phân trang và tìm kiếm."""
    page = int(request.args.get("page", 1))
    search_query = request.args.get("search", "").lower()

    if search_query:
        response = requests.get(f"{API_BASE}?limit=1000")
        data = response.json()
        all_pokemons = data["results"]
        filtered = [p for p in all_pokemons if search_query in p["name"]]
        total_count = len(filtered)
        total_pages = (total_count + PER_PAGE - 1) // PER_PAGE

        start = (page - 1) * PER_PAGE
        end = start + PER_PAGE
        paginated = filtered[start:end]

        pokemons = []
        for item in paginated:
            res = requests.get(item["url"])
            details = res.json()
            pokemons.append({
                "name": item["name"],
                "image": details["sprites"]["front_default"]
            })
    else:
        offset = (page - 1) * PER_PAGE
        response = requests.get(f"{API_BASE}?limit={PER_PAGE}&offset={offset}")
        data = response.json()

        pokemons = []
        for item in data["results"]:
            res = requests.get(item["url"])
            details = res.json()
            pokemons.append({
                "name": item["name"],
                "image": details["sprites"]["front_default"]
            })

        total_count = data["count"]
        total_pages = (total_count + PER_PAGE - 1) // PER_PAGE

    return render_template("index.html",
                           pokemons=pokemons,
                           page=page,
                           total_pages=total_pages,
                           search_query=search_query)

@app.route("/pokemon/<name>")
def pokemon_detail(name):
    """Hiển thị chi tiết Pokémon và chuỗi tiến hóa của nó."""
    response = requests.get(f"{API_BASE}{name}")
    if response.status_code != 200:
        return f"Không tìm thấy Pokémon {name}", 404

    data = response.json()

    # Lấy chuỗi tiến hóa
    evolutions = get_pokemon_evolution(data["species"]["url"])

    return render_template("detail.html", 
                           pokemon=data, 
                           evolutions=evolutions)

@app.route("/suggest")
def suggest():
    """Gợi ý các Pokémon khi người dùng tìm kiếm."""
    query = request.args.get("q", "").lower()
    if query:
        response = requests.get(f"{API_BASE}?limit=1000")
        data = response.json()
        all_pokemons = data["results"]
        matches = [p["name"] for p in all_pokemons if query in p["name"].lower()][:5]
        return jsonify(matches)
    return jsonify([])

if __name__ == "__main__":
    app.run(debug=True)
