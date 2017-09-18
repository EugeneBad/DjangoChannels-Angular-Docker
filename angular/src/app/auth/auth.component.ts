import { Component, OnInit } from '@angular/core';
import { root_url } from '../url';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css']
})
export class AuthComponent implements OnInit {

  passwordMismatch: boolean = false;
  duplicateUsername: boolean = false;

  signUsername: string;
  signPassword: string;
  confirmPassword: string;

  loginUsername: string;
  loginPassword: string;

  constructor() {

  }

  signUp(){
    if (this.signUsername && this.signPassword && this.confirmPassword){
      if (this.signPassword != this.confirmPassword){
        this.passwordMismatch = true;
        this.duplicateUsername = false;
      }
      if (this.signPassword == this.confirmPassword){
        this.passwordMismatch = false;
        this.duplicateUsername = false;

        let form = JSON.stringify({"username":this.signUsername,
         "password": this.signPassword})

        let signSocket = new WebSocket(root_url + "/register");
        signSocket.onopen = function(){ signSocket.send(form); }
        signSocket.onmessage = function(resp) {console.log(resp.data)}

      }
    }
  }

  ngOnInit() {
  }

}
