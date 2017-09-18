import { Component, OnInit, AfterViewChecked, Input, OnChanges, SimpleChanges } from '@angular/core';
import { root_url } from '../url';
import { Observable } from 'rxjs/Observable';
@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent implements OnInit, AfterViewChecked, OnChanges {

  token: string;
  fetchmsgSocket: any;

  fetchedMsgs: any;

  @Input () selectedUser;

  constructor() {}

  ngOnInit() {
    this.token = window.sessionStorage.getItem("token");
    let self = this;
    self.fetchmsgSocket = new WebSocket(root_url + `/fetch/msgs/${self.selectedUser}?` + self.token);
    self.fetchmsgSocket.onmessage = function(resp){
        self.fetchedMsgs = JSON.parse(resp.data);
        self.fetchmsgSocket.close();
      }
  }

  ngAfterViewChecked(){
    let chatdiv = document.getElementById("cont_div");
    chatdiv.scrollTop = chatdiv.scrollHeight;
  }

  ngOnChanges(changes: SimpleChanges){
    this.fetchedMsgs = [];
    let self = this;
    if (changes["selectedUser"]){

      self.fetchmsgSocket = new WebSocket(root_url + `/fetch/msgs/${self.selectedUser}?` + self.token);

      let observable = new Observable(observer => {
        self.fetchmsgSocket.onmessage = function(resp){
          observer.next(JSON.parse(resp.data));
        }
      });

      observable.subscribe(function(data){
        self.fetchedMsgs = data;
        self.fetchmsgSocket.close();})
    }
  }
}
