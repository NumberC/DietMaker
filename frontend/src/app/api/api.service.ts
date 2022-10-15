import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { UserData } from './api.types';
import { map } from 'rxjs'

const BACKEND_PORT = 5000;
const BACKEND_URL = 'http://loclhost:' + BACKEND_PORT +'/';

@Injectable({
  providedIn: 'root',
})
export class ApiService {

  constructor(private client: HttpClient) {

  }

  sendInfo(data: UserData) {
    return this.client.post(BACKEND_URL + '/createWeeklyMeal', {
      data
    }).pipe(
      map(res => res)
    )
  }

  getMenu(id: string) {
    return this.client.post(BACKEND_URL + '/getWeeklyMeal', {id})
  }
}
