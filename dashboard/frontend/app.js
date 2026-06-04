async function loadData(){

const response =
await fetch(
"http://localhost:8000/dashboard"
);

const data =
await response.json();

document.getElementById(
"backend"
).innerText =
data.backend;

document.getElementById(
"mqtt"
).innerText =
data.mqtt;

document.getElementById(
"command"
).innerText =
data.latest_command.command;

document.getElementById(
"confidence"
).innerText =
"Confidence: "
+ data.latest_command.confidence;
}

loadData();

setInterval(
loadData,
1000
);