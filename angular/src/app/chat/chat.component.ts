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
  textMsg: string = "";
  fetchmsgSocket: any;
  listenSocket: any;

  fetchedMsgs: any;

  @Input() selectedUser;

  constructor() { }

  ngOnInit() {
    this.token = window.sessionStorage.getItem("token");
    let self = this;
    self.fetchmsgSocket = new WebSocket(root_url + `/fetch/msgs/${self.selectedUser}?` + self.token);
    self.fetchmsgSocket.onmessage = function(resp) {
      self.fetchedMsgs = JSON.parse(resp.data);
      self.fetchmsgSocket.close();
    }
    this.listen();
  }

  ngAfterViewChecked() {
    let chatdiv = document.getElementById("cont_div");
    chatdiv.scrollTop = chatdiv.scrollHeight;
  }

  ngOnChanges(changes: SimpleChanges) {
    this.fetchedMsgs = [];
    let self = this;
    if (changes["selectedUser"]) {

      self.fetchmsgSocket = new WebSocket(root_url + `/fetch/msgs/${self.selectedUser}?` + self.token);

      let fetchObservable = new Observable(observer => {
        self.fetchmsgSocket.onmessage = function(resp) {
          observer.next(JSON.parse(resp.data));
        }
      });

      fetchObservable.subscribe(function(data) {
        self.fetchedMsgs = data;
        self.fetchmsgSocket.close();
      });
    }
  }

  listen() {
    this.listenSocket = new WebSocket(root_url + "/online?" + this.token);
    let self = this;

    let listenObservable = new Observable(observer => {
      self.listenSocket.onmessage = function(resp) {
        observer.next(JSON.parse(resp.data));
      }
    });

    listenObservable.subscribe(
      function(data) {
        if (data["status"] == "sent") {
          self.fetchedMsgs.push(data)

          let div = document.createElement('div');

          div.style.cssText = `background-color: khaki;
          color: black;
          padding: 5px;
          border-radius: 5px 0px 0px 5px;
          margin-top: 1%;
          width: ${data['width']}%;
          margin-left: ${data['margin']}%`

          div.innerHTML = `${self.textMsg}`

          document.getElementById('cont_div').appendChild(div);

        }
        // if (){
        //
        // }

      }
    );


  }

  send() {
    if (this.textMsg != "") {
      this.listenSocket.send(JSON.stringify({
        "token": this.token,
        "to": this.selectedUser,
        "body": this.textMsg
      }));
    }

  }

}
