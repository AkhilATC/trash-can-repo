import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ChandlerViewComponent } from './chandler-view/chandler-view.component';
import { LoginViewComponent } from './login-view/login-view.component';

const routes: Routes = [

  { path: 'chandler',component: ChandlerViewComponent},
  { path:'login', component: LoginViewComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
