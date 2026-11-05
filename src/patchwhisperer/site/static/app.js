(function () {
  "use strict";

  var POOL_KEY = "patchwhisperer:pool";
  var VIEW_KEY = "patchwhisperer:view";
  var BOARD_KEY = "patchwhisperer:board";
  var RANK_KEY = "patchwhisperer:rank";
  var BASE = window.PW_BASE || "";
  var HEROES = window.PW_POOL || [];
  var bySlug = {};
  HEROES.forEach(function (h) { bySlug[h.slug] = h; });

  function read(key) {
    try { return localStorage.getItem(key); } catch (e) { return null; }
  }
  function write(key, value) {
    try { localStorage.setItem(key, value); } catch (e) { /* page works without storage */ }
  }

  var memoryPool = null;
  function loadPool() {
    if (memoryPool) return memoryPool.slice();
    try {
      var v = JSON.parse(read(POOL_KEY));
      if (Array.isArray(v)) {
        return v.filter(function (s) { return bySlug[s]; });
      }
    } catch (e) { /* corrupt value means no pool */ }
    return [];
  }
  function savePool(ids) {
    memoryPool = ids.slice();
    write(POOL_KEY, JSON.stringify(ids));
  }

  function portraitEl(h, cls) {
    var p = document.createElement("span");
    p.className = "portrait " + (cls === undefined ? h.badge_class : cls);
    if (h.portrait) {
      var img = document.createElement("img");
      img.src = BASE + h.portrait;
      img.alt = "";
      img.width = 64;
      img.height = 64;
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

  /* pool band */

  var grid = document.getElementById("pool-grid");
  var empty = document.getElementById("pool-empty");
  var editBtn = document.getElementById("pool-edit");

  function renderPool() {
    var members = loadPool()
      .map(function (slug) { return bySlug[slug]; })
      .sort(function (a, b) {
        return a.pool_rank - b.pool_rank || a.name.localeCompare(b.name);
      });
    grid.innerHTML = "";
    members.forEach(function (h) {
      var a = document.createElement("a");
      a.className = "pool-hero";
      a.href = "#hero-" + h.slug;
      a.setAttribute("data-sheet", "hero-" + h.slug);
      a.appendChild(portraitEl(h));
      var name = document.createElement("span");
      name.className = "pool-name";
      name.textContent = h.name;
      var word = document.createElement("span");
      word.className = "badge " + h.badge_class;
      word.textContent = h.badge_word;
      a.appendChild(name);
      a.appendChild(word);
      grid.appendChild(a);
    });
    empty.hidden = members.length > 0;
    grid.hidden = members.length === 0;
    editBtn.textContent = members.length ? "Edit" : "Pick heroes";
  }

  /* picker */

  var picker = document.getElementById("pool-picker");
  var pickerGrid = document.getElementById("picker-grid");
  var view = read(VIEW_KEY) === "pool" ? "pool" : "all";

  function openPicker() {
    var pool = loadPool();
    pickerGrid.innerHTML = "";
    HEROES.forEach(function (h) {
      var b = document.createElement("button");
      var on = pool.indexOf(h.slug) >= 0;
      b.type = "button";
      b.className = "picker-hero" + (on ? " selected" : "");
      b.setAttribute("aria-pressed", on ? "true" : "false");
      b.appendChild(portraitEl(h, ""));
      var name = document.createElement("span");
      name.textContent = h.name;
      b.appendChild(name);
      b.addEventListener("click", function () {
        var cur = loadPool();
        var i = cur.indexOf(h.slug);
        if (i >= 0) cur.splice(i, 1);
        else cur.push(h.slug);
        savePool(cur);
        b.classList.toggle("selected", i < 0);
        b.setAttribute("aria-pressed", i < 0 ? "true" : "false");
      });
      pickerGrid.appendChild(b);
    });
    picker.showModal();
  }

  editBtn.addEventListener("click", openPicker);
  document.getElementById("picker-done").addEventListener("click", function () {
    picker.close();
  });
  picker.addEventListener("close", function () {
    renderPool();
    if (view === "pool" && !loadPool().length) view = "all";
    applyView();
  });

  /* tier list / what changed boards */

  var boardButtons = document.querySelectorAll("[data-board]");
  var board = read(BOARD_KEY) === "changes" ? "changes" : "tier";

  function applyBoard() {
    boardButtons.forEach(function (b) {
      b.setAttribute("aria-pressed", b.getAttribute("data-board") === board ? "true" : "false");
    });
    document.querySelectorAll("[data-board-pane]").forEach(function (p) {
      p.hidden = p.getAttribute("data-board-pane") !== board;
    });
  }

  var rankButtons = document.querySelectorAll("[data-rank]");
  var rankPanes = document.querySelectorAll("[data-rank-pane]");
  var rank = read(RANK_KEY);

  function applyRank() {
    var known = Array.prototype.some.call(rankPanes, function (p) {
      return p.getAttribute("data-rank-pane") === rank;
    });
    var active = known ? rank : rankPanes[0] && rankPanes[0].getAttribute("data-rank-pane");
    rankPanes.forEach(function (p) {
      p.hidden = p.getAttribute("data-rank-pane") !== active;
    });
    rankButtons.forEach(function (b) {
      b.setAttribute("aria-pressed", b.getAttribute("data-rank") === active ? "true" : "false");
    });
  }

  rankButtons.forEach(function (b) {
    b.addEventListener("click", function () {
      rank = b.getAttribute("data-rank");
      write(RANK_KEY, rank);
      applyRank();
    });
  });

  boardButtons.forEach(function (b) {
    b.addEventListener("click", function () {
      board = b.getAttribute("data-board");
      write(BOARD_KEY, board);
      applyBoard();
      applyView();
    });
  });

  /* everyone / my pool */

  var segButtons = document.querySelectorAll("[data-view]");
  var poolBand = document.getElementById("pool");

  function applyView() {
    var pool = loadPool();
    var mine = view === "pool" && pool.length > 0;
    segButtons.forEach(function (b) {
      b.setAttribute("aria-pressed", b.getAttribute("data-view") === (mine ? "pool" : "all") ? "true" : "false");
    });
    poolBand.hidden = view !== "pool";

    document.querySelectorAll("#heroes .tile").forEach(function (t) {
      t.hidden = mine && pool.indexOf(t.getAttribute("data-slug")) < 0;
    });
    document.querySelectorAll("#items .tile").forEach(function (t) {
      var hit = (t.getAttribute("data-heroes") || "").split(" ");
      t.hidden = mine && !hit.some(function (s) { return pool.indexOf(s) >= 0; });
    });

    ["heroes", "items"].forEach(function (id) {
      var section = document.getElementById(id);
      if (!section) return;
      var panes = section.querySelectorAll("[data-board-pane]");
      if (!panes.length) panes = [section];
      var any = false;
      panes.forEach(function (pane) {
        var paneAny = false;
        pane.querySelectorAll("[data-group]").forEach(function (g) {
          var n = g.querySelectorAll(".tile:not([hidden])").length;
          g.hidden = n === 0 || (!mine && g.hasAttribute("data-pool-only"));
          paneAny = paneAny || (n > 0 && !g.hidden);
          var c = g.querySelector("[data-count]");
          if (c) c.textContent = n;
        });
        if (!pane.hidden) any = any || paneAny;
      });
      var none = document.getElementById(id + "-empty");
      if (none) none.hidden = any;
    });

    document.querySelectorAll(".affected-hero").forEach(function (a) {
      a.classList.toggle("in-pool", pool.indexOf(a.getAttribute("data-slug")) >= 0);
    });
  }

  segButtons.forEach(function (b) {
    b.addEventListener("click", function () {
      view = b.getAttribute("data-view");
      write(VIEW_KEY, view);
      if (view === "pool" && !loadPool().length) {
        openPicker();
        return;
      }
      applyView();
    });
  });

  /* detail sheet, routed on the hash so a hero's card can be linked */

  var SHEET_ID = /^(hero|item|sys)-/;
  var sheet = document.getElementById("sheet");
  var body = document.getElementById("sheet-body");
  var pos = document.getElementById("sheet-pos");
  var prev = document.getElementById("sheet-prev");
  var next = document.getElementById("sheet-next");
  var current = null;
  var savedScroll = null;
  var ownEntry = false;

  function steps() {
    var scope = current && current.indexOf("item-") === 0 ? "#items"
      : current && current.indexOf("sys-") === 0 ? "#systems"
      : "#heroes [data-board-pane]:not([hidden])";
    return Array.prototype.filter.call(
      document.querySelectorAll(scope + " [data-sheet]:not([hidden])"),
      function (t) {
        var d = t.closest("details");
        return !(d && !d.open) && !t.closest("[hidden]");
      }
    ).map(function (t) { return t.getAttribute("data-sheet"); });
  }

  function showSheet(id) {
    var src = document.getElementById("sheet-" + id);
    if (!src) return false;
    if (sheet.open && current === id) return true;
    if (!sheet.open) savedScroll = window.scrollY;
    current = id;
    body.innerHTML = src.innerHTML;
    body.scrollTop = 0;
    var list = steps();
    var i = list.indexOf(id);
    prev.disabled = i <= 0;
    next.disabled = i < 0 || i >= list.length - 1;
    pos.textContent = i >= 0 ? (i + 1) + " of " + list.length : "";
    if (!sheet.open) {
      sheet.showModal();
      body.focus({ preventScroll: true });
    }
    return true;
  }

  function routeFromHash() {
    var id = location.hash.slice(1);
    if (!SHEET_ID.test(id) || !showSheet(id)) {
      if (sheet.open) sheet.close();
    }
  }

  function openFromLink(id) {
    if (!document.getElementById("sheet-" + id)) return;
    if (sheet.open) {
      history.replaceState(null, "", "#" + id);
      showSheet(id);
      return;
    }
    history.pushState({ sheet: id }, "", "#" + id);
    ownEntry = true;
    showSheet(id);
  }

  function requestClose() {
    if (!sheet.open) return;
    if (ownEntry) history.back();
    else sheet.close();
  }

  function step(delta) {
    var list = steps();
    var target = list[list.indexOf(current) + delta];
    if (target) history.replaceState(null, "", "#" + target), showSheet(target);
  }

  document.addEventListener("click", function (e) {
    if (e.defaultPrevented || e.button !== 0 ||
        e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    var link = e.target.closest ? e.target.closest("[data-sheet]") : null;
    if (!link) return;
    e.preventDefault();
    openFromLink(link.getAttribute("data-sheet"));
  });

  prev.addEventListener("click", function () { step(-1); });
  next.addEventListener("click", function () { step(1); });
  document.getElementById("sheet-close").addEventListener("click", requestClose);
  sheet.addEventListener("click", function (e) {
    if (e.target === sheet) requestClose();
  });
  sheet.addEventListener("cancel", function (e) {
    e.preventDefault();
    requestClose();
  });
  sheet.addEventListener("close", function () {
    current = null;
    ownEntry = false;
    body.innerHTML = "";
    if (SHEET_ID.test(location.hash.slice(1))) {
      history.replaceState(null, "", location.pathname + location.search);
    }
    if (savedScroll == null) return;
    var y = savedScroll;
    savedScroll = null;
    var root = document.documentElement;
    var smooth = root.style.scrollBehavior;
    root.style.scrollBehavior = "auto";
    window.scrollTo(0, y);
    requestAnimationFrame(function () {
      window.scrollTo(0, y);
      requestAnimationFrame(function () {
        window.scrollTo(0, y);
        root.style.scrollBehavior = smooth;
      });
    });
  });
  sheet.addEventListener("keydown", function (e) {
    if (e.key === "ArrowLeft") step(-1);
    if (e.key === "ArrowRight") step(1);
  });
  window.addEventListener("popstate", function (e) {
    ownEntry = !!(e.state && e.state.sheet);
    routeFromHash();
  });
  window.addEventListener("hashchange", routeFromHash);

  applyBoard();
  applyRank();
  renderPool();
  applyView();
  routeFromHash();
})();
