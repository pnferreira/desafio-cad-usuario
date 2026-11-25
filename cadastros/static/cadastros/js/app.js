const toggle = document.querySelector('[data-password]');
if (toggle) {
  toggle.addEventListener('click', () => {
    const senha = document.querySelector('input[name="senha"]');
    if (!senha) return;
    const tipo = senha.type === 'password' ? 'text' : 'password';
    document.querySelectorAll('input[name="senha"], input[name="confirmacao"]').forEach(campo => campo.type = tipo);
    toggle.textContent = tipo === 'password' ? 'Mostrar senha' : 'Ocultar senha';
  });
}
