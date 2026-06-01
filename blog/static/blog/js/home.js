const LIMIT_MOBILE = 100;
const LIMIT_DESKTOP = 400;

function getLimit() {
    return window.matchMedia("(max-width: 600px)").matches
        ? LIMIT_MOBILE
        : LIMIT_DESKTOP;
}

function applyTruncate() {
    const limit = getLimit();

    document.querySelectorAll(".preview-text").forEach(el => {
        if (!el.dataset.full) {
            el.dataset.full = el.textContent.trim();
        }

        const text = el.dataset.full;
        el.textContent = text.length > limit
            ? text.slice(0, limit) + "..."
            : text;
    });
}

applyTruncate();
window.addEventListener("resize", applyTruncate);