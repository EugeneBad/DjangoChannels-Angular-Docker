import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
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

  constructor(private router: Router) {

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
        let self = this;
        let signSocket = new WebSocket(root_url + "/register");
        signSocket.onopen = function(){ signSocket.send(form); }
        signSocket.onmessage = function(resp) {
          let response = JSON.parse(resp.data);
          if (response.status == "409"){
            self.duplicateUsername = true;
            signSocket.close();
          }
          if (response.status == "200"){
            signSocket.close();
            self.router.navigate(['/dashboard']);

          }
        }

      }
    }
  }

  ngOnInit() {
  }

}
