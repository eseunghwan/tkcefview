
function update_count(count) {
    document.getElementById("count").innerText = count;
}

function count_up() {
    MyAPI.count_up();
}

function count_down() {
    MyAPI.count_down();
}
