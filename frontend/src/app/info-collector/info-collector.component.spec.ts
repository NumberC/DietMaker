import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InfoCollectorComponent } from './info-collector.component';

describe('InfoCollectorComponent', () => {
  let component: InfoCollectorComponent;
  let fixture: ComponentFixture<InfoCollectorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ InfoCollectorComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(InfoCollectorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
