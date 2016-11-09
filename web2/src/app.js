import {Bookmark} from './bookmark';
import $ from 'jquery';

function reformatTime(datetime) {
  	var d = new Date(datetime)
  	return `${d.getHours()}:${d.getMinutes()}`;
  }

export class App {
  constructor() {
    this.heading = "Bookmarks";
    this.bookmarks = [];
  }

  addBookmark() {
    if (this.startStation && this.destinationStation) {
      this.bookmarks.push(new Bookmark(this.startStation, this.destinationStation));
    }
  }

  removeBookmark(bookmark) {
    let index = this.bookmarks.indexOf(bookmark);
    if (index !== -1) {
      this.bookmarks.splice(index, 1);
    }
  }

  swapDirections() {
  	[this.startStation, this.destinationStation] = [this.destinationStation, this.startStation]

  }

  nextConnection(bookmark) {
  	bookmark.journey = [];
  	var query = `http://transport.opendata.ch/v1/connections?from=${bookmark.start}&to=${bookmark.destination}&limit=1`;
  	$.get(query, fahrplan => {
  		for (var connection of fahrplan.connections) {
  			for (var section of connection.sections) {
  				if (section.journey == null) continue;
  				bookmark.journey.push(`Mit ${section.journey.name} ` +
  					`von ${section.departure.station.name} ` + 
  					`um ${reformatTime(section.departure.departure)} ` +
  					`nach ${section.journey.to} (${section.arrival.station.name} an: ${reformatTime(section.arrival.arrival)})`);
  			}
  		}
  	})
  }
}
