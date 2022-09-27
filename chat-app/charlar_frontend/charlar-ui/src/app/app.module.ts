import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { ChandlerViewComponent } from './chandler-view/chandler-view.component';
import { Routes, RouterModule } from '@angular/router';
import { LoginViewComponent } from './login-view/login-view.component';
import { HttpClientModule } from '@angular/common/http';
import { SignupComponent } from './signup/signup.component';

 
@NgModule({
  declarations: [
    AppComponent,
    ChandlerViewComponent,
    LoginViewComponent,
    SignupComponent
  ],
  imports: [
    
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
