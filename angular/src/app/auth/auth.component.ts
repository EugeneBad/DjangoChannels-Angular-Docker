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

  constructor() { }

  ngOnInit() {
  }

}
