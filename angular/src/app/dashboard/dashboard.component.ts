import { Component, OnInit } from '@angular/core';
import { root_url } from '../url';
import { Router } from '@angular/router';

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

  constructor(private router: Router) { }
// Try using an observable for route protection
  ngOnInit() {
    this.token = window.sessionStorage.getItem('token');
    if (!this.token){
      this.router.navigate(['/auth']);
    }
    else {
      let userSocket = new WebSocket(root_url + "/fetch/users/" + this.token);

      let self = this;
      userSocket.onmessage = function(resp){
      self.users = JSON.parse(resp.data);
      }
    }
  }

  showMsgs(event){
    this.selectedUser = event.target.innerText;
    this.showChat = true;
  }

  logOut(){
    sessionStorage.clear();
    this.router.navigate(['/auth']);
  }

}
