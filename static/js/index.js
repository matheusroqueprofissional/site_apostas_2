firebase.initializeApp(firebaseConfig);
firebase.auth().onAuthStateChanged(user=>{
    if(user){
        window.location.href = "/"
    }
})

function onChangeEmail(){
    toggleButtonsDisable();
    toggleEmailErrors();
}

function onChangePassword(){
    toggleButtonsDisable();
    togglePasswordErrors();
}



function login(){
    showloading()
    email = document.getElementById("email"),
    password = document.getElementById("password"),
    firebase.auth().signInWithEmailAndPassword(
        email.value,password.value
    ).then(response=>{
        hideLoading();
        window.location.href = "/"
    }).catch(error=>{
        hideLoading();
        alert(getErrorMessge(error))
    });
    
}

function getErrorMessge(error){
    if(error.code == "auth/user-not-found")
        return "Usuario não encontrado";
    
    if(error.code == "auth/invalid-email")
        return "Email invalido"
    if(error.code == "auth/internal-error")
        return "erro interno entre em contato com contato@thisme2.com"
    if(error.code == "auth/wrong-password")
        return "Usuario ou senha Incorretos"
        
    return error.message
}

function register(){
    window.location.href = "/registro"
}

function isEmailValid(){
const email = form.email().value;
if(!email){
    return false;
}
return validateEmail(email);
}

function recoverPassword(){
    showloading();
    email = document.getElementById("email")
    firebase.initializeApp(firebaseConfig);
    firebase.auth().sendPasswordResetEmail(email.value).then(()=>{
        hideLoading();
        alert("email enviado com sucesso\nverifique sua caixa de spam caso não encontre\ncaso não esteja na caixa de spam entre em contato com ...")
    }).catch(error =>{
        console.log("parte1")
        hideLoading();
        alert("erro ao enviar email: "+getErrorMessge(error))
    });
}

function toggleEmailErrors(){
    const email = form.email().value;
    form.emailRequiredError().style.display = email ? "none": "block";
    
    form.emailInvalidError().style.display = validateEmail(email) ? "none":"block";
}

function togglePasswordErrors(){
    const password = form.password().value;

    form.passwordRequiredError().style.display = password?"none":"block";
}

function toggleButtonsDisable(){
    const emailValid = isEmailValid();
    form.recoverPasswordButton().disabled = !emailValid;   
    
    const passwordValid = isPasswordValid()
    form.loginButton().disabled = !emailValid || !passwordValid;
}

function isPasswordValid(){
    const password = form.password().value;
    if(!password){
        return false;
    }
    return true;
}

function validateEmail(email){
    return /\S+@\S+\.\S+/.test(email);
}

const form = {
    email: () => document.getElementById("email"),
    emailInvalidError: () => document.getElementById("email-invalid-error"),
    emailRequiredError: () => document.getElementById("email-required-error"),
    loginButton: ()=> document.getElementById("login-button"),
    password: () => document.getElementById("password"),
    passwordRequiredError: ()=>document.getElementById("password-required-error"),
    recoverPasswordButton: () => document.getElementById("recover-password-button"),
}