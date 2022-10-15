import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CollectorFormComponent } from './collector-form.component';

describe('CollectorFormComponent', () => {
  let component: CollectorFormComponent;
  let fixture: ComponentFixture<CollectorFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CollectorFormComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CollectorFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
