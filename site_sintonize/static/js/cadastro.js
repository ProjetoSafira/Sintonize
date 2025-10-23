// Validação em Tempo Real do Formulário de Cadastro

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('cadastroForm');
    const emailInput = document.getElementById('email');
    const password1Input = document.getElementById('password1');
    const password2Input = document.getElementById('password2');
    const btnCadastrar = document.getElementById('btnCadastrar');
    
    // Elementos de requisitos
    const reqLength = document.getElementById('req-length');
    const reqSpecial = document.getElementById('req-special');
    const reqCase = document.getElementById('req-case');
    
    // Toggle de visibilidade da senha
    const toggleButtons = document.querySelectorAll('.toggle-password');
    
    toggleButtons.forEach(button => {
        button.addEventListener('click', function() {
            const targetId = this.getAttribute('data-target');
            const targetInput = document.getElementById(targetId);
            const eyeIcon = this.querySelector('.eye-icon');
            const eyeSlashIcon = this.querySelector('.eye-slash-icon');
            
            if (targetInput.type === 'password') {
                targetInput.type = 'text';
                eyeIcon.style.display = 'none';
                eyeSlashIcon.style.display = 'block';
            } else {
                targetInput.type = 'password';
                eyeIcon.style.display = 'block';
                eyeSlashIcon.style.display = 'none';
            }
        });
    });
    
    // Validação de E-mail
    emailInput.addEventListener('input', function() {
        validateEmail();
    });
    
    emailInput.addEventListener('blur', function() {
        validateEmail();
    });
    
    function validateEmail() {
        const emailValue = emailInput.value.trim();
        const emailError = document.getElementById('email-error');
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        
        if (emailValue === '') {
            emailInput.classList.remove('success', 'error');
            emailError.textContent = '';
            emailError.classList.remove('show');
            return false;
        }
        
        if (!emailRegex.test(emailValue)) {
            emailInput.classList.remove('success');
            emailInput.classList.add('error');
            emailError.textContent = 'Por favor, insira um e-mail válido.';
            emailError.classList.add('show');
            return false;
        } else {
            emailInput.classList.remove('error');
            emailInput.classList.add('success');
            emailError.textContent = '';
            emailError.classList.remove('show');
            return true;
        }
    }
    
    // Validação de Senha em Tempo Real
    password1Input.addEventListener('input', function() {
        validatePassword();
        validatePasswordMatch();
    });
    
    password1Input.addEventListener('blur', function() {
        validatePassword();
    });
    
    function validatePassword() {
        const passwordValue = password1Input.value;
        const passwordError = document.getElementById('password1-error');
        
        let isValid = true;
        const hasStartedTyping = passwordValue.length > 0;
        
        // Validar comprimento (mínimo 6 caracteres)
        if (passwordValue.length >= 6) {
            reqLength.classList.remove('invalid');
            reqLength.classList.add('valid');
        } else {
            reqLength.classList.remove('valid');
            if (hasStartedTyping) {
                reqLength.classList.add('invalid');
            } else {
                reqLength.classList.remove('invalid');
            }
            isValid = false;
        }
        
        // Validar caractere especial
        const specialCharRegex = /[!@#$%^&*(),.?":{}|<>]/;
        if (specialCharRegex.test(passwordValue)) {
            reqSpecial.classList.remove('invalid');
            reqSpecial.classList.add('valid');
        } else {
            reqSpecial.classList.remove('valid');
            if (hasStartedTyping) {
                reqSpecial.classList.add('invalid');
            } else {
                reqSpecial.classList.remove('invalid');
            }
            isValid = false;
        }
        
        // Validar maiúsculas e minúsculas
        const hasLowerCase = /[a-z]/.test(passwordValue);
        const hasUpperCase = /[A-Z]/.test(passwordValue);
        if (hasLowerCase && hasUpperCase) {
            reqCase.classList.remove('invalid');
            reqCase.classList.add('valid');
        } else {
            reqCase.classList.remove('valid');
            if (hasStartedTyping) {
                reqCase.classList.add('invalid');
            } else {
                reqCase.classList.remove('invalid');
            }
            isValid = false;
        }
        
        // Atualizar campo de senha
        if (passwordValue === '') {
            password1Input.classList.remove('success', 'error');
            passwordError.textContent = '';
            passwordError.classList.remove('show');
            return false;
        }
        
        if (isValid) {
            password1Input.classList.remove('error');
            password1Input.classList.add('success');
            passwordError.textContent = '';
            passwordError.classList.remove('show');
            return true;
        } else {
            password1Input.classList.remove('success');
            password1Input.classList.add('error');
            return false;
        }
    }
    
    // Validação de Confirmação de Senha
    password2Input.addEventListener('input', function() {
        validatePasswordMatch();
    });
    
    password2Input.addEventListener('blur', function() {
        validatePasswordMatch();
    });
    
    function validatePasswordMatch() {
        const password1Value = password1Input.value;
        const password2Value = password2Input.value;
        const password2Error = document.getElementById('password2-error');
        
        if (password2Value === '') {
            password2Input.classList.remove('success', 'error');
            password2Error.textContent = '';
            password2Error.classList.remove('show');
            return false;
        }
        
        if (password1Value !== password2Value) {
            password2Input.classList.remove('success');
            password2Input.classList.add('error');
            password2Error.textContent = 'As senhas não coincidem.';
            password2Error.classList.add('show');
            return false;
        } else {
            password2Input.classList.remove('error');
            password2Input.classList.add('success');
            password2Error.textContent = '';
            password2Error.classList.remove('show');
            return true;
        }
    }
    
    // Validação do Formulário antes de Enviar
    form.addEventListener('submit', function(e) {
        const isEmailValid = validateEmail();
        const isPasswordValid = validatePassword();
        const isPasswordMatchValid = validatePasswordMatch();
        
        if (!isEmailValid || !isPasswordValid || !isPasswordMatchValid) {
            e.preventDefault();
            
            // Mostrar mensagem de erro geral
            if (!isEmailValid) {
                emailInput.focus();
            } else if (!isPasswordValid) {
                password1Input.focus();
            } else if (!isPasswordMatchValid) {
                password2Input.focus();
            }
        }
    });
    
    // Animação de Loading no botão ao enviar
    form.addEventListener('submit', function() {
        btnCadastrar.disabled = true;
        btnCadastrar.textContent = 'Cadastrando...';
        
        // Reabilitar após 3 segundos caso haja erro
        setTimeout(function() {
            btnCadastrar.disabled = false;
            btnCadastrar.textContent = 'Cadastrar';
        }, 3000);
    });
});

