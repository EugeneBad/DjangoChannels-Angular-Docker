import { Routes, RouterModule } from '@angular/router'
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { AuthComponent } from './auth/auth.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { ChatComponent } from './chat/chat.component';

import { MdExpansionModule } from '@angular/material';

const appRoutes: Routes = [
  {
    path: 'auth',
    component: AuthComponent},
  {
    path: 'dashboard',
    component: DashboardComponent},
  {
    path: '**',
    redirectTo: 'dashboard',
    pathMatch: 'full'}
]

@NgModule({
  declarations: [
    AppComponent,
    AuthComponent,
    DashboardComponent,
    ChatComponent
  ],
  imports: [
    RouterModule.forRoot(appRoutes),
    BrowserModule,
    BrowserAnimationsModule,
    MdExpansionModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
