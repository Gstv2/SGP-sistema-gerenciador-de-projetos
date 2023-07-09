// Obter o elemento do botão "Adicionar coluna"
const addColumnButton = document.getElementById('add-column-btn');

// Obter o elemento do formulário de adição de coluna
const addColumnForm = document.getElementById('add-column-form');

// Obter o elemento do input de nome da coluna
const columnNameInput = document.getElementById('column-name');

// Adicionar o evento 'submit' no formulário de adição de coluna
addColumnForm.addEventListener('submit', addColumn);

// Adicionar o evento 'dragstart' em cada tarefa
document.addEventListener('dragstart', dragStart);

// Adicionar o evento 'dragover' em cada coluna
document.addEventListener('dragover', dragOver);

// Adicionar o evento 'drop' em cada coluna
document.addEventListener('drop', drop);

// Função para adicionar uma nova coluna ao quadro de projetos
function addColumn(e) {
  e.preventDefault();

  // Obter o nome da coluna do input
  const columnName = columnNameInput.value;

  // Criação dos elementos da coluna
  const column = document.createElement('div');
  const columnTitle = document.createElement('h2');
  const columnContent = document.createElement('div');
  const addTaskForm = document.createElement('form');
  const taskNameInput = document.createElement('input');
  const addTaskButton = document.createElement('button');

  // Adicionar as classes e os atributos aos elementos criados
  column.classList.add('column');
  column.setAttribute('draggable', 'true');
  columnTitle.innerText = columnName;
  columnContent.classList.add('column-content');
  addTaskForm.classList.add('add-task-form');
  taskNameInput.setAttribute('type', 'text');
  taskNameInput.setAttribute('placeholder', 'Digite o nome da tarefa');
  addTaskButton.innerText = 'Adicionar tarefa';

  // Adicionar os eventos aos elementos criados
  addTaskForm.addEventListener('submit', addTask);

  // Adicionar os elementos criados à coluna
  addTaskForm.appendChild(taskNameInput);
  addTaskForm.appendChild(addTaskButton);
  columnContent.appendChild(addTaskForm);
  column.appendChild(columnTitle);
  column.appendChild(columnContent);

  // Adicionar a nova coluna ao quadro de projetos
  const columnsContainer = document.getElementById('columns-container');
  columnsContainer.insertBefore(column, addColumnButton);

  // Limpar o valor do input de nome da coluna
  columnNameInput.value = '';
}

// Função para adicionar uma nova tarefa a uma coluna existente
function addTask(e) {
  e.preventDefault();

  // Obter o nome da tarefa do input
  const taskName = this.querySelector('input').value;

  // Criação do elemento da tarefa
  const task = document.createElement('div');
  task.classList.add('task');
  task.setAttribute('draggable', 'true');
  task.innerText = taskName;

  // Adicionar a nova tarefa à coluna correspondente
  const columnContent = this.parentNode;
  columnContent.insertBefore(task, this);

  // Limpar o valor do input de nome da tarefa
  this.querySelector('input').value = '';
}

// Função para iniciar a arrastar a tarefa ou a coluna
function dragStart(e) {
  if (e.target.classList.contains('task') || e.target.classList.contains('column')) {
    e.target.classList.add('dragging');
  }
}
