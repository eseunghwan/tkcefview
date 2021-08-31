
function update_count(count) {
    document.getElementById("count").innerText = count;
}

function count_up() {
    API.count_up();
}

function count_down() {
    API.count_down();
}
