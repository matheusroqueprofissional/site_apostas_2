firebase.initializeApp(firebaseConfig);

function logout(){
    firebase.auth().signOut().then(() => {
        window.location.href = "./login";
    }).catch(() => {
        alert('Erro ao fazer logout');
    })
}