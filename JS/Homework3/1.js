
const temperatureCel = Number.parseInt(prompt("Введите температуру в градусах Цельсия:"));
alert(`${temperatureCel} градусов по Цельсию - это ${tempFar(temperatureCel)} градусов по Фаренгейту`);

function tempFar(x) {
    let temperatureFar = (9 / 5) * x + 32;
    const roundTemperatureFar = temperatureFar.toFixed(2);
    return roundTemperatureFar
}
