const textarea = document.getElementById('notas');
const titulo = document.getElementById('container-TitleNotebook');
const lista = document.getElementById('listaNotas');

function cargarNotas() {
  lista.innerHTML = '';
  const notas = JSON.parse(localStorage.getItem('notasGuardadas')) || [];
  notas.forEach((nota, index) => {
    const li = document.createElement('li');
    li.textContent = `${nota.titulo} - ${nota.texto}`;
    lista.appendChild(li);
  });
}

document.getElementById('agregar').onclick = () => {
  const tituloValor = titulo.value.trim();
  const textoValor = textarea.value.trim();

  if (tituloValor && textoValor) {
    const notas = JSON.parse(localStorage.getItem('notasGuardadas')) || [];
    notas.push({ titulo: tituloValor, texto: textoValor });
    localStorage.setItem('notasGuardadas', JSON.stringify(notas));
    titulo.value = '';
    textarea.value = '';
    cargarNotas();
  } else {
    alert('Título y nota no pueden estar vacíos');
  }
};

document.getElementById('borrar').onclick = () => {
  if (confirm('¿Seguro que quieres borrar todas las notas?')) {
    localStorage.removeItem('notasGuardadas');
    lista.innerHTML = '';
  }
};

document.getElementById('descargar').onclick = () => {
  const notas = JSON.parse(localStorage.getItem('notasGuardadas')) || [];
  let contenido = '';
  notas.forEach((nota, i) => {
    contenido += `Nota ${i + 1} - ${nota.titulo}\n${nota.texto}\n\n`;
  });

  const blob = new Blob([contenido], { type: 'text/plain' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.download = 'mis_notas.txt';
  link.href = url;
  link.click();
  URL.revokeObjectURL(url);
};

window.onload = cargarNotas;
