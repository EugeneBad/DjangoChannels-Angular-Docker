import { Component, OnInit } from '@angular/core';
import { root_url } from '../url';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  showChat: boolean = false;

  token: string;
  users: any;

  selectedUser: string;

  constructor() { }
// Add an observable to integrate route protection
  ngOnInit() {
    this.token = window.sessionStorage.getItem('token');

    let userSocket = new WebSocket(root_url + "/fetch/users?" + this.token);

    let self = this;
    userSocket.onmessage = function(resp){
      self.users = JSON.parse(resp.data);
    }
  }

  showMsgs(event){
    this.selectedUser = event.target.innerText;
    this.showChat = true;
  }
}
