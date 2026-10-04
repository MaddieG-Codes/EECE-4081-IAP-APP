(async function () {
  const list = document.getElementById("location-list");
  const res = await fetch(list.dataset.apiUrl);
  if (!res.ok) {
    list.textContent = "Could not load locations.";
    return;
  }
  const { locations } = await res.json();
  for (const loc of locations) {
    const li = document.createElement("li");
    const a = document.createElement("a");
    a.href = `/locations/${loc.id}`;
    a.textContent = `${loc.name} (${loc.city})`;
    li.appendChild(a);
    list.appendChild(li);
  }
})();
