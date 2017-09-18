import { Component, OnInit, AfterViewChecked, Input } from '@angular/core';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent implements OnInit, AfterViewChecked {

  @Input () selectedUser;

  constructor() {}

  ngOnInit() {
  }

  ngAfterViewChecked(){
    let chatdiv = document.getElementById("cont_div");
    chatdiv.scrollTop = chatdiv.scrollHeight;
  }

}
