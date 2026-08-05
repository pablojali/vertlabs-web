// Búsqueda client-side simple sobre /search.json.
// A la escala de VertLabs (cientos de atletas, decenas de carreras)
// esto alcanza sin necesidad de un índice externo tipo Pagefind.

(async function () {
  const input = document.getElementById("search-input");
  const results = document.getElementById("search-results");
  if (!input || !results) return; // solo corre en /search/

  const res = await fetch("/search.json");
  const index = await res.json();

  input.addEventListener("input", () => {
    const q = input.value.trim().toLowerCase();
    results.innerHTML = "";
    if (!q) return;

    index
      .filter((item) => item.title.toLowerCase().includes(q))
      .slice(0, 20)
      .forEach((item) => {
        const li = document.createElement("li");
        li.innerHTML = `<a href="${item.url}">${item.title}</a> <span class="tag">${item.type}</span>`;
        results.appendChild(li);
      });
  });
})();
