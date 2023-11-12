
const form = document.createElement('form');
const input = document.createElement('input');
const button = document.createElement('button');
const resultDiv = document.createElement('div');

input.type = 'text';
button.type = 'submit';
button.textContent = 'Submit';

form.appendChild(input);
form.appendChild(button);
document.body.appendChild(form);

resultDiv.id = 'result';
document.body.appendChild(resultDiv);

button.addEventListener('click', async (event) => {
    event.preventDefault();
    const response = await fetch('/generate', {
        method: 'POST',
        body: JSON.stringify({ input: input.value }),
        headers: {
            'Content-Type': 'application/json'
        }
    });
    const data = await response.json();
    resultDiv.textContent = data.result;
});

