
function fetchJson(filename) {
    return fetch(filename)
        .then((res) => {
            return res.json();
        });
}

function getElapsedTime(node) {
    startTime = ("started_at" in node) ? node["started_at"] : node["created_at"];
    endTime = ("completed_at" in node) ? node["completed_at"] : node["updated_at"];
    return (Date.parse(endTime) - Date.parse(startTime));
}

function asMinutesSeconds(timestamp) {
    let dateStr = new Date(timestamp).toISOString().slice(14, 19);
    if (dateStr[0] == '0') {
        dateStr = dateStr.slice(1);
    }
    return dateStr;
}