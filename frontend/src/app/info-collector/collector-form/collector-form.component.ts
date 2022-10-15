import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-collector-form',
  templateUrl: './collector-form.component.html',
  styleUrls: ['./collector-form.component.css']
})
export class CollectorFormComponent implements OnInit {
  control: FormGroup;
  states: string[] = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

  constructor(private fb: FormBuilder) {
    this.control = fb.group({
      height: [null],
      weight: [null],
      age: [null],
      sex: [null],
      location: [null],
      budget: [null],
      dietaryRestrictions: [null]
    })
  }

  ngOnInit(): void {
  }

  handleSubmit() {
    console.log(this.control.value);
  }

}
