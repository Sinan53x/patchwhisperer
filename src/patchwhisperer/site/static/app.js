(function () {
  "use strict";

  var KEY = "patchwhisperer:pool";
  var BASE = window.PW_BASE || "";
  var HEROES = window.PW_POOL || [];

  function loadPool() {
    try {
      var raw = localStorage.getItem(KEY);
      var v = raw ? JSON.parse(raw) : null;
      if (!Array.isArray(v)) return null;
      return v.filter(function (s) { return typeof s === "string"; });
    } catch (e) {
      return null;
    }
  }

  function savePool(ids) {
    try {
      localStorage.setItem(KEY, JSON.stringify(ids));
    } catch (e) {
      /* storage may be unavailable; the page still works */
    }
  }

  var bySlug = {};
  HEROES.forEach(function (h) { bySlug[h.slug] = h; });

  function portraitEl(h, cls) {
    var p = document.createElement("span");
    p.className = "portrait " + (cls || h.badge_class);
    if (h.portrait) {
      var img = document.createElement("img");
      img.src = BASE + h.portrait;
      img.alt = h.name;
      img.width = 56;
      img.height = 56;
      p.appendChild(img);
    } else {
      var s = document.createElement("span");
      s.className = "initials";
      s.setAttribute("aria-hidden", "true");
      s.textContent = h.initials;
      p.appendChild(s);
    }
    return p;
  }

  /* -- pool section -- */

  var grid = document.getElementById("pool-grid");
  var empty = document.getElementById("pool-empty");

  function openHero(slug) {
    var card = document.getElementById("hero-" + slug);
    if (card) {
      card.hidden = false;
      card.open = true;
    }
  }

  function renderPool() {
    if (!grid || !empty) return;
    var pool = loadPool() || [];
    var members = pool
      .map(function (slug) { return bySlug[slug]; })
      .filter(Boolean)
      .sort(function (a, b) {
        return a.pool_rank - b.pool_rank || a.name.localeCompare(b.name);
      });
    grid.innerHTML = "";
    members.forEach(function (h) {
      var a = document.createElement("a");
      a.className = "pool-hero";
      a.href = "#hero-" + h.slug;
      a.appendChild(portraitEl(h));
      var name = document.createElement("span");
      name.className = "pool-name";
      name.textContent = h.name;
      var word = document.createElement("span");
      word.className = "badge " + h.badge_class;
      word.textContent = h.badge_word;
      a.appendChild(name);
      a.appendChild(word);
      a.addEventListener("click", function () { openHero(h.slug); });
      grid.appendChild(a);
    });
    empty.hidden = members.length > 0;
    grid.hidden = members.length === 0;
  }

  /* -- picker dialog -- */

  var dialog = document.getElementById("pool-picker");
  var pickerGrid = document.getElementById("picker-grid");
  var editBtn = document.getElementById("pool-edit");
  var doneBtn = document.getElementById("picker-done");

  function buildPicker() {
    if (!pickerGrid) return;
    var pool = loadPool() || [];
    pickerGrid.innerHTML = "";
    HEROES.forEach(function (h) {
      var selected = pool.indexOf(h.slug) >= 0;
      var b = document.createElement("button");
      b.type = "button";
      b.className = "picker-hero" + (selected ? " selected" : "");
      b.setAttribute("aria-pressed", selected ? "true" : "false");
      b.appendChild(portraitEl(h, ""));
      var name = document.createElement("span");
      name.textContent = h.name;
      b.appendChild(name);
      b.addEventListener("click", function () {
        var cur = loadPool() || [];
        var i = cur.indexOf(h.slug);
        if (i >= 0) cur.splice(i, 1);
        else cur.push(h.slug);
        savePool(cur);
        b.classList.toggle("selected", i < 0);
        b.setAttribute("aria-pressed", i < 0 ? "true" : "false");
      });
      pickerGrid.appendChild(b);
    });
  }

  if (editBtn && dialog) {
    editBtn.addEventListener("click", function () {
      buildPicker();
      if (dialog.showModal) dialog.showModal();
      else dialog.setAttribute("open", "");
    });
  }
  if (doneBtn && dialog) {
    doneBtn.addEventListener("click", function () {
      if (dialog.close) dialog.close();
      else dialog.removeAttribute("open");
    });
    dialog.addEventListener("close", renderPool);
  }

  /* -- hero filters -- */

  var chips = document.querySelectorAll(".chip[data-filter]");
  var inNotes = document.getElementById("in-notes");
  var filter = "all";

  function applyFilters() {
    var onlyNotes = !inNotes || inNotes.checked;
    document.querySelectorAll(".hero-card").forEach(function (card) {
      var ok = true;
      if (filter === "keep" || filter === "watch" || filter === "bench") {
        ok = card.getAttribute("data-verdict") === filter;
      } else if (filter === "up" || filter === "down") {
        ok = card.getAttribute("data-direction") === filter;
      }
      if (ok && onlyNotes) {
        ok = card.getAttribute("data-in-notes") === "1";
      }
      card.hidden = !ok;
    });
  }

  chips.forEach(function (c) {
    c.addEventListener("click", function () {
      filter = c.getAttribute("data-filter");
      chips.forEach(function (x) {
        x.classList.toggle("active", x === c);
      });
      applyFilters();
    });
  });
  if (inNotes) inNotes.addEventListener("change", applyFilters);

  renderPool();
  applyFilters();
})();
