document.addEventListener("DOMContentLoaded", function () {
    const input = document.getElementById("pokemonInput");
    const suggestionBox = document.getElementById("suggestions");

    input.addEventListener("input", function () {
        const query = input.value.trim();
        console.log("Đang tìm kiếm với từ khóa:", query);  // Log giá trị từ khóa tìm kiếm
        if (query.length === 0) {
            suggestionBox.innerHTML = "";
            return;
        }

        fetch(`/suggest?q=${query}`)
            .then(res => res.json())
            .then(data => {
                console.log("Kết quả gợi ý:", data);  // Log kết quả từ API
                suggestionBox.innerHTML = "";
                if (data.length > 0) {
                    data.forEach(name => {
                        const div = document.createElement("div");
                        div.textContent = name;
                        div.addEventListener("click", () => {
                            input.value = name;
                            suggestionBox.innerHTML = "";
                        });
                        suggestionBox.appendChild(div);
                    });
                } else {
                    suggestionBox.innerHTML = "<div>Không có kết quả tìm kiếm.</div>";
                }
            })
            .catch(error => {
                console.error('Lỗi:', error);
                suggestionBox.innerHTML = "<div>Đã xảy ra lỗi.</div>";
            });
    });
});
