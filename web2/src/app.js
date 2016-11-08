import {Bookmark} from './bookmark';

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

  nextConnection() {

  }
}
