import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login-view',
  templateUrl: './login-view.component.html',
  styleUrls: ['./login-view.component.scss']
})
export class LoginViewComponent implements OnInit {
  
  public userName:string;
  public passWord: string;
  public msg:string;
  constructor( private _router: Router) { }
  ngOnInit(): void {
  }

  public logIn(){

    console.log(this.passWord,this.userName);
    this.msg = "Failed";
    localStorage.setItem('user',this.userName);
    this._router.navigateByUrl('/chandler');
   

  }

}
