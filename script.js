function playerChoice(choice) {
    fetch(`/play/${choice}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerText = `Player chose ${data.player_choice}, Computer chose ${data.computer_choice}. ${data.result}`;
        });
}
