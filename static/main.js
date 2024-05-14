
// Events

function load_data(url, target) {
    fetch(url)
        .then((resp) => resp.json())
        .then(function(data) {
            console.log("Data -> ", data.data);
            document.getElementById(target).innerHTML = `<p>${data.data}</p>`;
    }).catch(function(error) {
        console.log(error);
    });
}

function argumentos(url, target, argumento) {
    fetch(url + `?nome=${argumento}`)
        .then((resp) => resp.json())
        .then(function(data) {
            console.log("Data -> ", data.data);
            document.getElementById(target).innerHTML = `<p style="text-wrap: wrap; width: 100px;">${data.data}</p>`;
    }).catch(function(error) {
        console.log(error);
    });
}

function idades_sexo(url, target) {
    fetch(url)
        .then((resp) => resp.json())
        .then(function(data) {
            console.log("Data -> ", data.data);
            dado = data.data;
            content = `<p><strong>Homens:</strong> ${dado.homens['%']}%</p>`;
            content += `<p><strong>Mulheres:</strong> ${dado.mulheres['%']}%</p>`;
            document.getElementById(target).innerHTML = content;
    }).catch(function(error) {
        console.log(error);
    });
}

function salarios(url, target) {
    fetch(url)
        .then((resp) => resp.json())
        .then(function(data) {
            console.log("Data -> ", data.data);
            dado = data.data;
            content = `<p><strong>Registros:</strong> ${dado.registros}</p>`;
            content += `<p><strong>Registros:</strong> ${dado.porcentagem}%</p>`;
            content += `<p><strong>Total:</strong> ${dado.total}</p>`;
            document.getElementById(target).innerHTML = content;
    }).catch(function(error) {
        console.log(error);
    });
}

function maiores_salarios(url, target) {
    fetch(url)
        .then((resp) => resp.json())
        .then(function(data) {
            console.log("Data -> ", data.data);
            dado = data.data;
            content =  `<p><strong>1°:</strong> (${dado.pessoa1.id}) ${dado.pessoa1.nome} - ${dado.pessoa1.salario}</p>`;
            content += `<p><strong>2°:</strong> (${dado.pessoa2.id}) ${dado.pessoa2.nome} - ${dado.pessoa2.salario}</p>`;
            content += `<p><strong>3°:</strong> (${dado.pessoa3.id}) ${dado.pessoa3.nome} - ${dado.pessoa3.salario}}</p>`;
            document.getElementById(target).innerHTML = content;
    }).catch(function(error) {
        console.log(error);
    });
}