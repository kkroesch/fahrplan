    
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

  removeTodo(todo) {
    let index = this.todos.indexOf(todo);
    if (index !== -1) {
      this.todos.splice(index, 1);
    }
  }
}
