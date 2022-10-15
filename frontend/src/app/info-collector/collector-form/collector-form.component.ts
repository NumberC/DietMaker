import { Component, OnInit, ElementRef, ViewChild } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import {COMMA, ENTER} from '@angular/cdk/keycodes';
import {FormControl} from '@angular/forms';
import {MatAutocompleteSelectedEvent} from '@angular/material/autocomplete';
import {MatChipInputEvent} from '@angular/material/chips';
import {Observable} from 'rxjs';
import {map, startWith} from 'rxjs/operators';
import { ApiService } from 'src/app/api/api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-collector-form',
  templateUrl: './collector-form.component.html',
  styleUrls: ['./collector-form.component.css']
})
export class CollectorFormComponent implements OnInit {  
  control: FormGroup;

  separatorKeysCodes: number[] = [ENTER, COMMA];
  filteredFruits: Observable<string[]>;
  fruits: string[] = [];
  allFruits: string[] = ['peanuts', 'tree nuts','wheat / has celiac disease', 'milk / is lactose intolerant', 'eggs', 'soy', 'fish', 'shellfish', 'sesame seeds'];
  fruitCtrl = new FormControl('');

  @ViewChild('fruitInput') fruitInput?: ElementRef<HTMLInputElement>;

  constructor(private fb: FormBuilder, private api: ApiService, private router: Router) {
    this.control = this.fb.group({
      height: [null],
      weight: [null],
      age: [null],
      sex: [null],
      budget: [null],
      dietaryRestrictions: [null]
    })

    this.filteredFruits = this.fruitCtrl.valueChanges.pipe(
      startWith(null),
      map((fruit: string | null) => (fruit ? this._filter(fruit) : this.allFruits.slice())),
    );
  }

  ngOnInit(): void {
  }

  selected(event: MatAutocompleteSelectedEvent): void {
    this.fruits.push(event.option.viewValue);
    if (!this.fruitInput) return
    this.fruitInput.nativeElement.value = '';
    this.fruitCtrl.setValue(null);
  }

  add(event: MatChipInputEvent): void {
    const value = (event.value || '').trim();

    // Add our fruit
    if (value) {
      this.fruits.push(value);
    }

    // Clear the input value
    event.chipInput!.clear();

    this.fruitCtrl.setValue(null);
  }

  remove(fruit: string): void {
    const index = this.fruits.indexOf(fruit);

    if (index >= 0) {
      this.fruits.splice(index, 1);
    }
  }


  handleSubmit() {
    console.log(this.control.value, this.fruits);
    const data = this.control.value;
    data.dietaryRestrictions = this.fruits;
    this.api.sendInfo(data)
    .subscribe(res => {
      this.router.navigate(['/view'])
    })
  }

  private _filter(value: string): string[] {
    const filterValue = value.toLowerCase();

    return this.allFruits.filter(fruit => fruit.toLowerCase().includes(filterValue));
  }

}
