const AuthorController = require('../controllers/author.controller');

module.exports = (app) => {
    app.get('/api/authors', AuthorController.getAll);
    app.post('/api/authors/new', AuthorController.create);
    app.get('/api/authors/:id', AuthorController.getOne);
    app.patch('/api/authors/:id/edit', AuthorController.update);
    app.delete('/api/authors/delete/:id', AuthorController.delete);
}
