import { ChatServiceService } from './../_service/chat-service.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-chandler-view',
  templateUrl: './chandler-view.component.html',
  styleUrls: ['./chandler-view.component.scss']
})
export class ChandlerViewComponent implements OnInit {


  public chat_info :any= []

  constructor(public chatServiceService: ChatServiceService) { }

  ngOnInit(): void {
    this.loadChats()
  }
  
  loadChats(){
    this.chatServiceService.fetch_nodes()
          .subscribe((data)=>{
            this.chat_info =  data;
          },error  => {
            console.log(error)            
            });

  }
  deleteNote(noteId){
    console.log(noteId);
  }

}
