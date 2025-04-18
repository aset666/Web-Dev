import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './views/auth/login.component';
import { TaskBoardComponent } from './views/tasks/task-board.component';

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'board', component: TaskBoardComponent },
  { path: '', redirectTo: 'login', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
