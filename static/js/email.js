function sendEmail() {
    const email = document.querySelector("email").value;
    const nome = document.querySelector("nome").value;
    
    if (email === "" || nome === "") {
      alert("Preencha todos os campos!");
      return;
    }
    
    // Código para enviar o email utilizando o pacote nodemailer
  }