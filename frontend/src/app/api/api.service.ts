import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { UserData } from './api.types';
import { map } from 'rxjs'

const BACKEND_PORT = 5000;
const BACKEND_URL = 'http://loclhost:' + BACKEND_PORT +'/';

/*
Array of 7 arrays. Each of those arrays has 3 arrays for each meal.
Each of those arrays has 2 food items.
[
  [
    [Breakfast1, Breakfast2],
    [Lunch1, Lunch2],
    [Dinner1, Dinner2]
  ],
  [],
  [],
  [],
  [],
  [],
  []
]

Each food item looks like this:
{
  fdcId: ???,
  description: i treat this like it's the name,
  dataType: who cares
  .. more useless info ..
  foodNutrients: [
    food nutrients if you care
  ]
}

*/

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  id: string = '';

  constructor(private client: HttpClient) {

  }

  sendInfo(data: UserData) {
    return this.client.post(BACKEND_URL + '/createWeeklyMeal', {
      data
    }).pipe(
      map(res => {
        this.id = 'idSet';
        return res;
      })
    )
  }

  getId(): false | string {
    return this.id != '' && this.id;
  }

  getMenu(id: string) {
    return this.client.post(BACKEND_URL + '/getWeeklyMeal', {id})
  }
}
