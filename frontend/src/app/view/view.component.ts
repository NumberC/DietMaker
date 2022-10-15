import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api/api.service';

@Component({
  selector: 'app-view',
  templateUrl: './view.component.html',
  styleUrls: ['./view.component.css']
})
export class ViewComponent implements OnInit {
  schedule = this.api.getMenu('3209831')

  constructor(private api: ApiService) { }

  ngOnInit(): void {
  }

}
