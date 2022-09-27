import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { ChandlerViewComponent } from './chandler-view/chandler-view.component';
import { Routes, RouterModule } from '@angular/router';
import { LoginViewComponent } from './login-view/login-view.component';

 const appRoutes: Routes = [
 
  { path: 'chandler',component: ChandlerViewComponent}
];
@NgModule({
  declarations: [
    AppComponent,
    ChandlerViewComponent,
    LoginViewComponent
  ],
  imports: [
    RouterModule.forRoot(appRoutes),
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
