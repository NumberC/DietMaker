import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InfoCollectorComponent } from './info-collector/info-collector.component';
import { ViewComponent } from './view/view.component';

const routes: Routes = [
  {path:'view', component: ViewComponent},
  {path:'', component: InfoCollectorComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
