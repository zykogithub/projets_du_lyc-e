<!DOCTYPE html>
<html lang="fr"><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">

    <title>période 2/</title>
    <link id="favicon" rel="shortcut icon" type="image/x-icon" href="http://localhost:8888/static/base/images/favicon.ico?v=97c6417ed01bdc0ae3ef32ae4894fd03">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="gluton1_fichiers/jquery-ui.css" type="text/css">
    <link rel="stylesheet" href="gluton1_fichiers/jquery.css" type="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    
    <link rel="stylesheet" href="gluton1_fichiers/style.css" type="text/css">
    
    <link rel="stylesheet" href="gluton1_fichiers/custom.css" type="text/css">
    <script src="gluton1_fichiers/promise.js" type="text/javascript" charset="utf-8"></script>
    <script src="gluton1_fichiers/react.js" type="text/javascript"></script>
    <script src="gluton1_fichiers/react-dom.js" type="text/javascript"></script>
    <script src="gluton1_fichiers/index.js" type="text/javascript"></script>
    <script src="gluton1_fichiers/require.js" type="text/javascript" charset="utf-8"></script>
    <script>
      require.config({
          
          urlArgs: "v=20220412165142",
          
          baseUrl: '/static/',
          paths: {
            'auth/js/main': 'auth/js/main.min',
            custom : '/custom',
            nbextensions : '/nbextensions',
            kernelspecs : '/kernelspecs',
            underscore : 'components/underscore/underscore-min',
            backbone : 'components/backbone/backbone-min',
            jed: 'components/jed/jed',
            jquery: 'components/jquery/jquery.min',
            json: 'components/requirejs-plugins/src/json',
            text: 'components/requirejs-text/text',
            bootstrap: 'components/bootstrap/dist/js/bootstrap.min',
            bootstraptour: 'components/bootstrap-tour/build/js/bootstrap-tour.min',
            'jquery-ui': 'components/jquery-ui/jquery-ui.min',
            moment: 'components/moment/min/moment-with-locales',
            codemirror: 'components/codemirror',
            termjs: 'components/xterm.js/xterm',
            typeahead: 'components/jquery-typeahead/dist/jquery.typeahead.min',
          },
          map: { // for backward compatibility
              "*": {
                  "jqueryui": "jquery-ui",
              }
          },
          shim: {
            typeahead: {
              deps: ["jquery"],
              exports: "typeahead"
            },
            underscore: {
              exports: '_'
            },
            backbone: {
              deps: ["underscore", "jquery"],
              exports: "Backbone"
            },
            bootstrap: {
              deps: ["jquery"],
              exports: "bootstrap"
            },
            bootstraptour: {
              deps: ["bootstrap"],
              exports: "Tour"
            },
            "jquery-ui": {
              deps: ["jquery"],
              exports: "$"
            }
          },
          waitSeconds: 30,
      });

      require.config({
          map: {
              '*':{
                'contents': 'services/contents',
              }
          }
      });

      // error-catching custom.js shim.
      define("custom", function (require, exports, module) {
          try {
              var custom = require('custom/custom');
              console.debug('loaded custom.js');
              return custom;
          } catch (e) {
              console.error("error loading custom.js", e);
              return {};
          }
      })

    document.nbjs_translations = {"domain": "nbjs", "locale_data": {"nbjs": {"": {"domain": "nbjs"}, "Manually edit the JSON below to manipulate the metadata for this cell.": ["\u00c9diter manuellement le JSON ci-dessous pour manipuler les m\u00e9ta-donn\u00e9es de cette cellule"], "Manually edit the JSON below to manipulate the metadata for this notebook.": ["\u00c9diter manuellement le JSON ci-dessous pour manipuler les m\u00e9ta-donn\u00e9es de ce notebook."], " We recommend putting custom metadata attributes in an appropriately named substructure, so they don't conflict with those of others.": [" Il est recommand\u00e9 de placer les attributs personnalis\u00e9s de m\u00e9ta-donn\u00e9es dans une sous-structure nomm\u00e9e de mani\u00e8re appropri\u00e9e, afin qu'ils n'interf\u00e8rent pas avec ceux des autres."], "Edit the metadata": ["\u00c9diter les m\u00e9ta-donn\u00e9es"], "Edit Notebook Metadata": ["\u00c9diter les m\u00e9ta-donn\u00e9es du Notebook"], "Edit Cell Metadata": ["\u00c9diter les m\u00e9ta-donn\u00e9es de la cellule"], "Cancel": ["Annuler"], "Edit": ["\u00c9diter"], "OK": ["OK"], "Apply": ["Appliquer"], "WARNING: Could not save invalid JSON.": ["ATTENTION: Impossible de sauvegarder du JSON invalide."], "There are no attachments for this cell.": ["Il n'y a pas de pi\u00e8ce-jointe \u00e0 cette cellule."], "Current cell attachments": ["Pi\u00e8ce-jointes actuelles de la cellule"], "Attachments": ["Pi\u00e8ces jointes"], "Restore": ["Restaurer"], "Delete": ["Supprimer"], "Edit attachments": ["Modifier les pi\u00e8ces jointes"], "Edit Notebook Attachments": ["Modifier les pi\u00e8ces jointes du Notebook"], "Edit Cell Attachments": ["Modifier les pi\u00e8ces jointes de la cellule"], "Select a file to insert.": ["S\u00e9lectionner un fichier \u00e0 ins\u00e9rer."], "Select a file": ["S\u00e9lectionner un fichier"], "You are using Jupyter notebook.": ["Vous utilisez un notebook Jupyter."], "The version of the notebook server is: ": ["La version du serveur de notebook est : "], "The server is running on this version of Python:": ["Le serveur utilise la version de Python :"], "Waiting for kernel to be available...": ["En attente de disponibilit\u00e9 du noyau..."], "Server Information:": ["Information du serveur :"], "Current Kernel Information:": ["Information du Noyau courant :"], "Could not access sys_info variable for version information.": ["Impossible d'acc\u00e9der \u00e0 la variable sys_info pour l'information relative aux versions."], "Cannot find sys_info!": ["Impossible de trouver sys_info !"], "About Jupyter Notebook": ["\u00c0 propos de Jupyter Notebook"], "unable to contact kernel": ["impossible de joindre le noyau"], "toggle rtl layout": ["Changer le sens d'organisation de l'interface"], "Toggle the screen directionality between left-to-right and right-to-left": ["Changer le sens d'organisation des \u00e9l\u00e9ments d'interface entre gauche-\u00e0-droite et droite-\u00e0-gauche"], "edit command mode keyboard shortcuts": ["modifier les raccourcis clavier du mode commande"], "Open a dialog to edit the command mode keyboard shortcuts": ["Ouvrir un dialogue pour \u00e9diter les racourcis clavier du mode commande"], "restart kernel": ["red\u00e9marrer le noyau"], "restart the kernel (no confirmation dialog)": ["red\u00e9marrer le noyau (sans confirmation)"], "confirm restart kernel": ["confirmer le red\u00e9marrage du noyau"], "restart the kernel (with dialog)": ["red\u00e9marrer le noyau (avec confirmation)"], "restart kernel and run all cells": ["red\u00e9marrer le noyau et ex\u00e9cuter toutes les cellules"], "restart the kernel, then re-run the whole notebook (no confirmation dialog)": ["red\u00e9marrer le noyau, et r\u00e9-ex\u00e9cuter tout le notebook (sans confirmation)"], "confirm restart kernel and run all cells": ["confirmer le red\u00e9marrage du noyau et l'ex\u00e9cution des cellules"], "restart the kernel, then re-run the whole notebook (with dialog)": ["red\u00e9marrer le noyau, et r\u00e9-ex\u00e9cuter tout le notebook (sans confirmation)"], "restart kernel and clear output": ["red\u00e9marrer le noyau, et effacer les sorties"], "restart the kernel and clear all output (no confirmation dialog)": ["red\u00e9marrer le noyau et effacer les sorties (sans confirmation)"], "confirm restart kernel and clear output": ["confirmer le red\u00e9marrage du noyau et l'effacement des sorties"], "restart the kernel and clear all output (with dialog)": ["red\u00e9marrer le noyau et effacer les sorties (avec confirmation)"], "interrupt the kernel": ["interrompre le noyau"], "run cell and select next": ["ex\u00e9cuter la cellule et s\u00e9lectionner la suivante"], "run cell, select below": ["ex\u00e9cuter la cellule, s\u00e9lectionner la suivante"], "run selected cells": ["ex\u00e9cuter les cellules s\u00e9lectionn\u00e9es"], "run cell and insert below": ["ex\u00e9cuter la cellule et ins\u00e9rer apr\u00e8s"], "run all cells": ["ex\u00e9cuter toutes les cellules"], "run all cells above": ["ex\u00e9cuter toutes les cellules pr\u00e9c\u00e9dentes"], "run all cells below": ["Ex\u00e9cuter toutes les cellules suivantes"], "enter command mode": ["ouvrir le mode commande"], "insert image": ["ins\u00e9rer une image"], "cut cell attachments": ["couper les pi\u00e8ces-jointes de la cellule"], "copy cell attachments": ["copier les pi\u00e8ces-jointes de la cellule"], "paste cell attachments": ["coller les pi\u00e8ces-jointes de la cellule"], "split cell at cursor": ["s\u00e9parer la cellule au niveau du curseur"], "enter edit mode": ["activer le mode d'\u00e9dition"], "select previous cell": ["s\u00e9lectionner la cellule pr\u00e9c\u00e9dente"], "select cell above": ["s\u00e9lectionner la cellule pr\u00e9c\u00e9dente"], "select next cell": ["s\u00e9lectionner la cellule suivante"], "select cell below": ["s\u00e9lectionner la cellule suivante"], "extend selection above": ["\u00e9tendre la s\u00e9lection vers le haut"], "extend selected cells above": ["\u00e9tendre les cellules s\u00e9lectionn\u00e9es vers le haut"], "extend selection below": ["\u00e9tendre la s\u00e9lection vers le bas"], "extend selected cells below": ["\u00e9tendre les cellules s\u00e9lectionn\u00e9es vers le bas"], "cut selected cells": ["couper les cellules s\u00e9lectionn\u00e9es"], "copy selected cells": ["copier les cellules s\u00e9lectionn\u00e9es"], "paste cells above": ["coller les cellules avant"], "paste cells below": ["coller les cellules apr\u00e8s"], "insert cell above": ["ins\u00e9rer une cellule avant"], "insert cell below": ["ins\u00e9rer une cellule apr\u00e8s"], "change cell to code": ["transformer en cellule de code"], "change cell to markdown": ["transformer celllule en markdown"], "change cell to raw": ["transformer en texte brut (pour NBConvert)"], "change cell to heading 1": ["transformer en titre de niveau 1"], "change cell to heading 2": ["transformer en titre de niveau 2"], "change cell to heading 3": ["transformer en titre de niveau 3"], "change cell to heading 4": ["transformer en titre de niveau 4"], "change cell to heading 5": ["transformer en titre de niveau 5"], "change cell to heading 6": ["transformer en titre de niveau 6"], "toggle cell output": ["afficher/masquer la sortie de cellule"], "toggle output of selected cells": ["afficher/masquer la sortie des cellules s\u00e9lectionn\u00e9es"], "toggle cell scrolling": ["afficher/masquer la barre de d\u00e9filement de la sortie de la cellule"], "toggle output scrolling of selected cells": ["afficher/masquer la barre de d\u00e9filement des la sortie des cellules s\u00e9lectionn\u00e9es"], "clear cell output": ["effacer la sortie de la cellule"], "clear output of selected cells": ["effacer la sortie des cellules s\u00e9lectionn\u00e9es"], "move cells down": ["d\u00e9placer les cellules vers le bas"], "move selected cells down": ["d\u00e9placer les cellules s\u00e9lectionn\u00e9es vers le bas"], "move cells up": ["d\u00e9placer les cellules vers le haut"], "move selected cells up": ["d\u00e9placer les cellules s\u00e9lectionn\u00e9es vers le haut"], "toggle line numbers": ["afficher/masquer les num\u00e9ros de ligne"], "show keyboard shortcuts": ["afficher les raccourcis clavier"], "delete cells": ["supprimer les cellules"], "delete selected cells": ["supprimer les cellules s\u00e9lectionn\u00e9es"], "undo cell deletion": ["annuler la suppression de cellule"], "merge cell with previous cell": ["fusionner la cellule avec la pr\u00e9c\u00e9dente"], "merge cell above": ["fusionner la cellule avec les pr\u00e9c\u00e9dentes"], "merge cell with next cell": ["fusionner la cellule avec la suivante"], "merge cell below": ["fusionner la cellule avec les suivantes"], "merge selected cells": ["fusionnnner les cellules s\u00e9lectionn\u00e9es"], "merge cells": ["fusionnnner les cellules"], "merge selected cells, or current cell with cell below if only one cell is selected": ["fusionner les cellules s\u00e9lectionn\u00e9es, ou la cellule courante avec la suivante si une unique cellule est s\u00e9lectionn\u00e9e"], "show command pallette": ["afficher la palette de commandes"], "open the command palette": ["ouvrir la palette de commandes"], "toggle all line numbers": ["afficher/masquer tous les num\u00e9ros de ligne"], "toggles line numbers in all cells, and persist the setting": ["afficher/masquer les num\u00e9ros de ligne dans toutes ces cellules, et s'en souvenir dans les param\u00e8tres"], "show all line numbers": ["afficher/masquer tous les num\u00e9ros de ligne"], "show line numbers in all cells, and persist the setting": ["afficher les num\u00e9ros de ligne dans toutes les cellules, et s'en souvenir dans les param\u00e8tres"], "hide all line numbers": ["masquer tous les num\u00e9ros de ligne"], "hide line numbers in all cells, and persist the setting": ["masquer les num\u00e9ros de ligne dans toutes les cellules, et s'en souvenir dans les param\u00e8tres"], "toggle header": ["afficher/masquer l'en-t\u00eate"], "switch between showing and hiding the header": ["afficher/masquer l'en-t\u00eate"], "show the header": ["afficher l'en-t\u00eate"], "hide the header": ["masquer l'en-t\u00eate"], "toggle toolbar": ["afficher/masquer la barre d'outils"], "switch between showing and hiding the toolbar": ["afficher/masquer la barre d'outils"], "show the toolbar": ["afficher la barre d'outils"], "hide the toolbar": ["masquer la barre d'outils"], "close the pager": ["fermer le paginateur"], "ignore": ["ignorer"], "move cursor up": ["d\u00e9placer le curseur vers le haut"], "move cursor down": ["d\u00e9placer le curseur vers le bas"], "scroll notebook down": ["faire d\u00e9filer le notebook vers le bas"], "scroll notebook up": ["faire d\u00e9filer le notebook vers le haut"], "scroll cell center": ["faire d\u00e9filer la cellule courante au centre"], "Scroll the current cell to the center": ["Faire d\u00e9filer la cellule courante au centre"], "scroll cell top": ["faire d\u00e9filer la cellule en haut"], "Scroll the current cell to the top": ["Faire d\u00e9filer la cellule courante en haut"], "duplicate notebook": ["dupliquer le notebook"], "Create and open a copy of the current notebook": ["Cr\u00e9er et ouvrir une copie du notebook courant"], "trust notebook": ["faire confiance \u00e0 ce notebook"], "Trust the current notebook": ["Faire confiance au notebook courant"], "rename notebook": ["renommer le notebook"], "Rename the current notebook": ["Renommer le notebook courant"], "toggle all cells output collapsed": ["afficher/masquer toutes les sorties en mode compact"], "Toggle the hidden state of all output areas": ["Afficher/masquer toutes les sorties"], "toggle all cells output scrolled": ["afficher/masquer toutes les sorties en mode d\u00e9filement"], "Toggle the scrolling state of all output areas": ["Activer/d\u00e9sactiver le d\u00e9filement de toutes les sorties"], "clear all cells output": ["effacer le contenu de toutes les sorties de cellules"], "Clear the content of all the outputs": ["Effacer le contenu de toutes les sorties"], "save notebook": ["enregistrer le notebook"], "Save and Checkpoint": ["Cr\u00e9er une nouvelle sauvegarde"], "Warning: accessing Cell.cm_config directly is deprecated.": ["Attention : acc\u00e9der \u00e0 Cell.cm_config directement est d\u00e9pr\u00e9ci\u00e9."], "Unrecognized cell type: %s": ["Type de cellule non reconnu : %s"], "Unrecognized cell type": ["Type de cellule non reconnu"], "Error in cell toolbar callback %s": ["Erreur dans le callback %s de la barre d'outil de cellule"], "Clipboard types: %s": ["Types de donn\u00e9es dans le presse-papier : %s"], "Dialog for paste from system clipboard": ["Bo\u00eete de dialogue pour coller depuis le presse-papier du syst\u00e8me"], "Ctrl-V": ["Ctrl-V"], "Cmd-V": ["Cmd-V"], "Press %s again to paste": ["Appuyer sur %s \u00e0 nouveau pour coller"], "Why is this needed? ": ["Pourquoi ce comportement ?"], "We can't get paste events in this browser without a text box. ": ["Il n'est pas possible de capturer les \u00e9v\u00e8nements \u00ab coller \u00bb dans le navigateur sans champ de texte"], "There's an invisible text box focused in this dialog.": ["Cette bo\u00eete de dialogue contient un champ de texte invisible."], "%s to paste": ["%s pour coller"], "Can't execute cell since kernel is not set.": ["Impossible d'ex\u00e9cuter cette cellule car aucun noyau n'est choisi."], "In": ["Entr\u00e9e"], "Could not find a kernel matching %s. Please select a kernel:": ["Impossible de trouver un noyau correspondant \u00e0 %s. Merci de s\u00e9lectionner un noyau :"], "Continue Without Kernel": ["Poursuivre sans noyau"], "Set Kernel": ["Choisir le noyau"], "Kernel not found": ["Noyau introuvable"], "Creating Notebook Failed": ["La cr\u00e9ation du notebook a \u00e9chou\u00e9"], "The error was: %s": ["L'erreur est : %s"], "Run": ["Ex\u00e9cuter"], "Code": ["Code"], "Markdown": ["Markdown"], "Raw NBConvert": ["Texte Brut (pour NBConvert)"], "Heading": ["Titre"], "unrecognized cell type:": ["type de cellule non reconnu :"], "Failed to retrieve MathJax from '%s'": ["Impossible de r\u00e9cup\u00e9rer MathJax depuis '%s'"], "Math/LaTeX rendering will be disabled.": ["Le rendu Math/LaTex sera d\u00e9sactiv\u00e9."], "Trusted Notebook": ["Notebook de confiance"], "Trust Notebook": ["Faire confiance \u00e0 ce Notebook"], "None": ["Aucun(e)"], "No checkpoints": ["Pas de point de sauvegarde"], "Opens in a new window": ["Ouvrir dans une nouvelle fen\u00eatre"], "Autosave in progress, latest changes may be lost.": ["Auto-sauvegarde en cours, les derni\u00e8res modifications pourraient \u00eatre perdues."], "Unsaved changes will be lost.": ["Les modifications non sauvegard\u00e9es seront perdues."], "The Kernel is busy, outputs may be lost.": ["Le noyau est occup\u00e9, les sorties pourraient \u00eatre perdues."], "This notebook is version %1$s, but we only fully support up to %2$s.": ["Ce notebook est pr\u00e9vu pour la version %1$s du logiciel, mais nous supportons au maximum la version %2$s."], "You can still work with this notebook, but cell and output types introduced in later notebook versions will not be available.": ["Vous pouvez continuer \u00e0 travailler avec ce notebook, mais les types de cellules et de sorties introduits dans les versions ult\u00e9rieures du logiciel ne seront pas disponibles."], "Restart and Run All Cells": ["Relancer et ex\u00e9cuter toutes les cellules"], "Restart and Clear All Outputs": ["Relancer et effacer toutes les sorties"], "Restart": ["Relancer"], "Continue Running": ["Poursuivre l'ex\u00e9cution"], "Reload": ["Recharger"], "Overwrite": ["\u00c9craser"], "Trust": ["Faire confiance"], "Revert": ["R\u00e9tablir"], "Newer Notebook": ["Notebook plus r\u00e9cent"], "Use markdown headings": ["Utiliser les titres markdown"], "Jupyter no longer uses special heading cells. Instead, write your headings in Markdown cells using # characters:": ["Jupyter n'utilise plus de cellules sp\u00e9ciales pour les titres. \u00c0 la place, utiliser la syntaxe de titre dans des cellules Markdown avec les caract\u00e8res # :"], "## This is a level 2 heading": ["## Ceci est un titre de niveau 2"], "Restart kernel and re-run the whole notebook?": ["Red\u00e9marrer le noyau et r\u00e9-ex\u00e9cuter l'ensemble du noteboook ?"], "Are you sure you want to restart the current kernel and re-execute the whole notebook?  All variables and outputs will be lost.": ["\u00cates-vous certain de vouloir red\u00e9marrer le noyau actuel et r\u00e9-ex\u00e9cuter l'ensemble du notebook ? Toutes les variables et sorties seront perdues."], "Restart kernel and clear all output?": ["Red\u00e9marrer le noyau et effacer toutes les sorties ?"], "Do you want to restart the current kernel and clear all output?  All variables and outputs will be lost.": ["Souhaitez-vous red\u00e9marrer le noyau actuel et effacer toutes les sorties ? Toutes les variables et les sorties seront perdues."], "Restart kernel?": ["Red\u00e9marrer le noyau ?"], "Do you want to restart the current kernel?  All variables will be lost.": ["Souhaitez-vous red\u00e9marrer le noyau actuel ? Toutes les variables seront perdues."], "Shutdown kernel?": ["Arr\u00eater le noyau ?"], "Do you want to shutdown the current kernel?  All variables will be lost.": ["Souhaitez-vous red\u00e9marrer le noyau actuel ? Toutes les variables seront perdues."], "Notebook changed": ["Notebook modifi\u00e9"], "The notebook file has changed on disk since the last time we opened or saved it. Do you want to overwrite the file on disk with the version open here, or load the version on disk (reload the page) ?": ["Le fichier du notebook a chang\u00e9 sur le disque depuis que vous l'avez ouvert ou sauvegard\u00e9. Souhaitez-vous \u00e9craser le fichier sur le disque avec la version ouverte ici ou charger la version pr\u00e9sente sur le disque (recharge la page) ?"], "Notebook validation failed": ["La validation du notebook a \u00e9chou\u00e9"], "The save operation succeeded, but the notebook does not appear to be valid. The validation error was:": ["La sauvegarde a r\u00e9ussi, mais le notebook semble invalide. L'erreur de validation est :"], "A trusted Jupyter notebook may execute hidden malicious code when you open it. Selecting trust will immediately reload this notebook in a trusted state. For more information, see the Jupyter security documentation: ": ["Un notebook Jupyter auquel vous faites confiance peut ex\u00e9cuter du code malicieux quand vous l'ouvrez. Choisir de faire confiance \u00e0 ce notebook va le recharger imm\u00e9diatement en mode confiance. Pour davantage d'information, voir la section s\u00e9curit\u00e9 dans la documentation de Jupyter."], "here": ["ici"], "Trust this notebook?": ["Faire confiance \u00e0 ce notebook ?"], "Notebook failed to load": ["Le chargement du notebook a \u00e9chou\u00e9"], "The error was: ": ["L'erreur est : "], "See the error console for details.": ["Voir la console d'erreur pour davantage de d\u00e9tails."], "The notebook also failed validation:": ["La validation du notebook a \u00e9chou\u00e9 :"], "An invalid notebook may not function properly. The validation error was:": ["Un notebook non valide peut dysfonctionner. L'erreur de validation est :"], "This notebook has been converted from an older notebook format to the current notebook format v(%s).": ["Ce notebook a \u00e9t\u00e9 converti depuis un format plus ancien de notebook vers le format actuel v(%s)."], "This notebook has been converted from a newer notebook format to the current notebook format v(%s).": ["Ce notebook a \u00e9t\u00e9 converti depuis un format plus r\u00e9cent de notebook vers le format actuel v(%s)."], "The next time you save this notebook, the current notebook format will be used.": ["Au prochain enregistrement de ce notebook, le format actuel de notebook sera utilis\u00e9"], "Older versions of Jupyter may not be able to read the new format.": ["D'anciennes version de Jupyter peuvent ne pas \u00eatre en mesure de lire le nouveau format."], "Some features of the original notebook may not be available.": ["Certaines fonctionalit\u00e9s du notebook d'origine peuvent ne pas \u00eatre disponibles."], "To preserve the original version, close the notebook without saving it.": ["Pour pr\u00e9server la version originale, fermer le notebook sans l'enregistrer."], "Notebook converted": ["Notebook converti"], "(No name)": ["(Sans nom)"], "An unknown error occurred while loading this notebook. This version can load notebook formats %s or earlier. See the server log for details.": ["Une erreur inconnue s'est produite pendant le chargement de ce notebook. Cette version peut charger des formats de notebooks %s ou plus ancien. Voir les journaux du serveur pour davantage d'information."], "Error loading notebook": ["Erreur pendant le chargement du notebook"], "Are you sure you want to revert the notebook to the latest checkpoint?": ["\u00cates-vous certain de vouloir restaurer la derni\u00e8re sauvegarde ?"], "This cannot be undone.": ["Impossible d'annuler."], "The checkpoint was last updated at:": ["Derni\u00e8re sauvegarde \u00e0 : "], "Revert notebook to checkpoint": ["Restaurer le notebook \u00e0 une sauvegarde ant\u00e9rieure"], "Edit Mode": ["Mode \u00c9dition"], "Command Mode": ["Mode Commande"], "Kernel Created": ["Noyau cr\u00e9\u00e9"], "Connecting to kernel": ["Connexion au noyau"], "Not Connected": ["Non connect\u00e9"], "click to reconnect": ["cliquer pour reconnecter"], "Restarting kernel": ["Noyau en cours de red\u00e9marrage"], "Kernel Restarting": ["Noyau en cours de red\u00e9marrage"], "The kernel appears to have died. It will restart automatically.": ["Le noyau semble plant\u00e9. Il va red\u00e9marrer automatiquement."], "Dead kernel": ["Noyau plant\u00e9"], "Kernel Dead": ["Noyau plant\u00e9"], "Interrupting kernel": ["Noyau en cours d'interruption"], "No Connection to Kernel": ["Pas de connexion au noyau"], "A connection to the notebook server could not be established. The notebook will continue trying to reconnect. Check your network connection or notebook server configuration.": ["La connexion au serveur de notebook ne peut pas \u00eatre \u00e9tablie. Le notebook va continuer ses tentatives. V\u00e9rifiez votre connexion r\u00e9seau ou les param\u00e8tres du serveur de notebook."], "Connection failed": ["\u00c9chec de la connexion"], "No kernel": ["Pas de noyau"], "Kernel is not running": ["Le noyau n'est pas actif"], "Don't Restart": ["Ne pas red\u00e9marrer"], "Try Restarting Now": ["Essayer de red\u00e9marrer maintenant"], "The kernel has died, and the automatic restart has failed. It is possible the kernel cannot be restarted. If you are not able to restart the kernel, you will still be able to save the notebook, but running code will no longer work until the notebook is reopened.": ["Le noyau a plant\u00e9, et le red\u00e9marrage automatique a \u00e9chou\u00e9. Il est possible que le noyau ne puisse pas \u00eatre relanc\u00e9. Si c'est le cas, vous pourrez toujours sauvegarder le notebook, mais l'ex\u00e9cution de code ne fonctionnera pas jusqu'\u00e0 la r\u00e9-ouverture du notebook."], "No Kernel": ["Pas de Noyau"], "Failed to start the kernel": ["\u00c9chec du d\u00e9marrage du noyau"], "Kernel Busy": ["Noyau occup\u00e9"], "Kernel starting, please wait...": ["Noyau en cours de d\u00e9marrage, patientez\u2026"], "Kernel Idle": ["Noyau inactif"], "Kernel ready": ["Noyau pr\u00eat"], "Using kernel: ": ["Noyau utilis\u00e9 : "], "Only candidate for language: %1$s was %2$s.": ["Unique candidat pour le langage : %1$s \u00e9tait %2$s."], "Loading notebook": ["Chargement du notebook en cours"], "Notebook loaded": ["Notebook charg\u00e9"], "Saving notebook": ["Enregistrement du notebook en cours"], "Notebook saved": ["Notebook enregistr\u00e9"], "Notebook save failed": ["L'enregistrement du notebook a \u00e9chou\u00e9"], "Notebook copy failed": ["La copie du notebook a \u00e9chou\u00e9"], "Checkpoint created": ["Sauvegarde cr\u00e9\u00e9e"], "Checkpoint failed": ["\u00c9chec de la sauvegarde"], "Checkpoint deleted": ["Sauvegarde supprim\u00e9e"], "Checkpoint delete failed": ["\u00c9chec de la suppression de la sauvegarde"], "Restoring to checkpoint...": ["Restauration de la sauvegarde..."], "Checkpoint restore failed": ["La restauration de la sauvegarde a \u00e9chou\u00e9"], "Autosave disabled": ["Sauvegarde automatique d\u00e9sactiv\u00e9e"], "Saving every %d sec.": ["Sauvegarde toutes les %d sec."], "Trusted": ["Fiable"], "Not Trusted": ["Non fiable"], "click to expand output": ["cliquer pour afficher toute la sortie"], "click to expand output; double click to hide output": ["cliquer pour afficher toute la sortie ; double-cliquer pour masquer la sortie"], "click to unscroll output; double click to hide": ["cliquer pour faire d\u00e9filer la sortie vers le haut ; double-cliquer pour masquer"], "click to scroll output; double click to hide": ["cliquer pour faire d\u00e9filer la sortie ; double-cliquer pour masquer"], "Javascript error adding output!": ["Erreur JavaScript pendant l'\u00e9criture de la sortie !"], "See your browser Javascript console for more details.": ["Voir la console JavaScript de votre navigateur pour plus d'informations."], "Out[%d]:": ["Sortie[%d] :"], "Unrecognized output: %s": ["Sortie non reconnue : %s"], "Open the pager in an external window": ["Ouvrir le paginateur dans une fen\u00eatre externe"], "Close the pager": ["Fermer le paginateur"], "Jupyter Pager": ["Paginateur de Jupyter"], "go to cell start": ["aller au d\u00e9but de la cellule"], "go to cell end": ["aller \u00e0 la fin de la cellule"], "go one word left": ["se d\u00e9placer d'un mot vers la gauche"], "go one word right": ["Se d\u00e9placer d'un mot vers la droite"], "delete word before": ["supprimer le mot pr\u00e9c\u00e9dent"], "delete word after": ["supprimer le mot suivant"], "code completion or indent": ["compl\u00e9tion de code ou indentation"], "tooltip": ["info-bulle"], "indent": ["indenter"], "dedent": ["d\u00e9-indenter"], "select all": ["tout s\u00e9lectionner"], "undo": ["annuler"], "redo": ["refaire"], "Shift": ["Maj"], "Alt": ["Alt"], "Up": ["Haut"], "Down": ["Bas"], "Left": ["Gauche"], "Right": ["Droite"], "Tab": ["Tab"], "Caps Lock": ["Verr. Maj."], "Esc": ["Esc"], "Ctrl": ["Ctrl"], "Enter": ["Entr\u00e9e"], "Page Up": ["Page Pr\u00e9c."], "Page Down": ["Page Suiv."], "Home": ["Accueil"], "End": ["Fin"], "Space": ["Espace"], "Backspace": ["Retour arri\u00e8re"], "Minus": ["Moins"], "PageUp": ["PagePr\u00e9c."], "The Jupyter Notebook has two different keyboard input modes.": ["Le Notebook Jupyter offre deux modes de saisie claivier."], "<b>Edit mode</b> allows you to type code or text into a cell and is indicated by a green cell border.": ["<b>Mode \u00c9dition</b> permet de saisir du code ou du texte dans une cellule et se reconna\u00eet \u00e0 la bordure verte de la cellule."], "<b>Command mode</b> binds the keyboard to notebook level commands and is indicated by a grey cell border with a blue left margin.": ["<b>Mode Commande</b> d\u00e9clenche au clavier des actions au niveau du notebook et se reconna\u00eet \u00e0 la bordure grise de la cellule, avec une marge bleue sur la droite."], "Close": ["Fermer"], "Keyboard shortcuts": ["Raccourcis clavier"], "Command": ["Commande"], "Control": ["Contr\u00f4les"], "Option": ["Option"], "Return": ["Retour"], "Command Mode (press %s to enable)": ["Mode Commande (presser %s pour l'activer)"], "Edit Shortcuts": ["Modifier les Raccourcis Clavier"], "edit command-mode keyboard shortcuts": ["modifier les raccourcis clavier du mode commande"], "Edit Mode (press %s to enable)": ["Mode \u00c9dition (presser %s pour l'activer)"], "Autosave Failed!": ["\u00c9chec de la sauvegarde automatique !"], "Rename": ["Renommer"], "Enter a new notebook name:": ["Saisir le nouveau nom du notebook"], "Rename Notebook": ["Renommer le Notebook"], "Invalid notebook name. Notebook names must have 1 or more characters and can contain any characters except :/\\. Please enter a new notebook name:": ["Nom de notebook invalide. Les noms de notebooks doivent poss\u00e9der au moins un caract\u00e8re et peuvent contenir tous les caract\u00e8res sauf \u00ab /\\ \u00bb. Merci de saisir un nouveau nom de notebook :"], "Renaming...": ["Renommage en cours..."], "Unknown error": ["Erreur inconnue"], "no checkpoint": ["aucune sauvegarde"], "Last Checkpoint: %s": ["Derni\u00e8re Sauvegarde : %s"], "(unsaved changes)": ["(modifi\u00e9)"], "(autosaved)": ["(auto-sauvegard\u00e9)"], "Warning: too many matches (%d). Some changes might not be shown or applied.": ["Attention : trop de correspondances (%d). Certains changements peuvent ne pas \u00eatre affich\u00e9s ou appliqu\u00e9s."], "%d match": ["%d correspondance", "%d correspondances"], "More than 100 matches, aborting": ["Plus de 100 correspondances, annulation"], "Use regex (JavaScript regex syntax)": ["Utiliser des regex (syntaxe des regex JavaScript)"], "Replace in selected cells": ["Remplacer dans les cellules s\u00e9lectionn\u00e9es"], "Match case": ["Sensible \u00e0 la casse"], "Find": ["Rechercher"], "Replace": ["Remplacer"], "No matches, invalid or empty regular expression": ["Aucune correspondance trouv\u00e9e, expression r\u00e9guli\u00e8re vide ou invalide."], "Replace All": ["Tout Remplacer"], "Find and Replace": ["Rechercher et Remplacer"], "find and replace": ["rechercher et remplacer"], "Write raw LaTeX or other formats here, for use with nbconvert. It will not be rendered in the notebook. When passing through nbconvert, a Raw Cell's content is added to the output unmodified.": ["\u00c9crivez ici du code Latex brut ou d'autres formats, pour usage avec nbconvert. Il ne sera pas rendu dans le notebook. En utilisant nbconvert, le contenu d'une cellule brute est ajout\u00e9 tel-quel \u00e0 la sortie."], "Grow the tooltip vertically (press shift-tab twice)": ["Agrandir l'info-bulle verticallement (presser Maj-Tab deux fois)"], "show the current docstring in pager (press shift-tab 4 times)": ["montrer la cha\u00eene de documentation courante dans le paginateur (presser shift-tab 4 fois)"], "Open in Pager": ["Ouvrir dans le Paginateur"], "Tooltip will linger for 10 seconds while you type": ["L'info-bulle restera affich\u00e9e 10 secondes pendant votre saisie"], "Welcome to the Notebook Tour": ["Bienvenue dans la visite du Notebook"], "You can use the left and right arrow keys to go backwards and forwards.": ["Vous pouvez utiliser les touches gauche et droite pour continuer ou revenir en arri\u00e8re."], "Filename": ["Nom du fichier"], "Click here to change the filename for this notebook.": ["Cliquer ici pour changer le nom du fichier de ce notebook."], "Notebook Menubar": ["Barre de Menu du Notebook"], "The menubar has menus for actions on the notebook, its cells, and the kernel it communicates with.": ["La barre de menu a des menus pour les actions concernant le notebook, ses cellules, et le noyau avec lequel il communique."], "Notebook Toolbar": ["Barre d'outils du Notebook"], "The toolbar has buttons for the most common actions. Hover your mouse over each button for more information.": ["La barre d'outils a des boutons pour les actions les plus fr\u00e9quentes. Survoler les boutons \u00e0 la souris pour plus d'information."], "Mode Indicator": ["Indicateur de mode"], "The Notebook has two modes: Edit Mode and Command Mode. In this area, an indicator can appear to tell you which mode you are in.": ["Le Notebook offre deux modes : \u00c9dition et Commande. Dans cette zone, un indicateur peut vous indiquer dans quel mode vous \u00eates."], "Right now you are in Command Mode, and many keyboard shortcuts are available. In this mode, no icon is displayed in the indicator area.": ["Actuellement, vous \u00eates en mode Commande, et de nombreux raccourcis clavier sont disponibles. Dans ce mode, aucune ic\u00f4ne n'est affich\u00e9e dans la zone d'indication."], "Pressing <code>Enter</code> or clicking in the input text area of the cell switches to Edit Mode.": ["Presser <code>Entr\u00e9e</code> ou cliquer dans la zone de saisie de la cellule bascule vers le Mode \u00c9dition."], "Notice that the border around the currently active cell changed color. Typing will insert text into the currently active cell.": ["Notez que la bordure autour de la cellule active a chang\u00e9 de couleur. Saisir du texte au clavier l'ins\u00e9rera dans la cellule active."], "Back to Command Mode": ["Retourner au Mode Commande"], "Pressing <code>Esc</code> or clicking outside of the input text area takes you back to Command Mode.": ["Presser <code>Esc</code> ou cliquer en dehors de la zone de saisie de la cellule vous ram\u00e8ne au Mode Commande."], "Keyboard Shortcuts": ["Raccourcis Clavier"], "You can click here to get a list of all of the keyboard shortcuts.": ["Vous pouvez cliquer ici pour afficher une liste de tous les raccourcis clavier."], "Kernel Indicator": ["Indicateur de Noyau"], "This is the Kernel indicator. It looks like this when the Kernel is idle.": ["Ceci est l'indicateur de Noyau. Il a cet aspect quand le Noyau est inactif."], "The Kernel indicator looks like this when the Kernel is busy.": ["L'indicateur de Noyau a cet aspect quand le Noyau est actif."], "Interrupting the Kernel": ["Interrompre le Noyau"], "To cancel a computation in progress, you can click here.": ["Pour annuler une ex\u00e9cution en cours, vous pouvez cliquer ici."], "Notification Area": ["Zone de notification"], "Messages in response to user actions (Save, Interrupt, etc.) appear here.": ["Les messages en retour d'actions utilisateur (Enregistrement, Interruption, etc.) s'affichent ici."], "End of Tour": ["Fin de la visite"], "This concludes the Jupyter Notebook User Interface Tour.": ["C'est la fin de cette visite guid\u00e9e de l'Interface utilisateur du Notebook Jupyter."], "Edit Attachments": ["Modifier les Pi\u00e8ces-Jointes"], "Cell": ["Cellule"], "Edit Metadata": ["\u00c9diter les M\u00e9ta-Donn\u00e9es"], "Custom": ["Personnalis\u00e9"], "Set the MIME type of the raw cell:": ["D\u00e9finir le type MIME de la cellule en texte brut :"], "Raw Cell MIME Type": ["Type MIME de la Cellule en Texte Brut"], "Raw NBConvert Format": ["Format du Texte Brut"], "Raw Cell Format": ["Format de la Cellule Texte Brut"], "Slide": ["Diapo"], "Sub-Slide": ["Sous-Diapo"], "Fragment": ["Extrait"], "Skip": ["Sauter"], "Notes": ["Notes"], "Slide Type": ["Type de diapo"], "Slideshow": ["Diaporama"], "Add tag": ["Ajouter un mot-cl\u00e9"], "Edit the list of tags below. All whitespace is treated as tag separators.": ["Modifier la liste de mots-cl\u00e9s ci-dessous. Les espaces sont consid\u00e9r\u00e9s comme des s\u00e9parateurs."], "Edit the tags": ["Modifier les mots-cl\u00e9s"], "Edit Tags": ["Modifier Mots-Cl\u00e9s"], "Shutdown": ["Arr\u00eater"], "Create a new notebook with %s": ["Cr\u00e9er un nouveau notebook avec %s"], "An error occurred while creating a new notebook.": ["Une erreur s'est produite \u00e0 la cr\u00e9ation du notebook"], "Creating File Failed": ["La cr\u00e9ation du fichier a \u00e9chou\u00e9"], "An error occurred while creating a new file.": ["Une erreur est survenue \u00e0 la cr\u00e9ation du nouveau fichier."], "Creating Folder Failed": ["La cr\u00e9ation du r\u00e9pertoire a \u00e9chou\u00e9"], "An error occurred while creating a new folder.": ["Une erreur est survenue \u00e0 la cr\u00e9ation du nouveau r\u00e9pertoire."], "Failed to read file": ["\u00c9chec de lecture du fichier"], "Failed to read file %s": ["\u00c9chec de lecture du fichier %s"], "The file size is %d MB. Do you still want to upload it?": ["Le fichier p\u00e8se %d MB. \u00cates-vous certain de vouloir le t\u00e9l\u00e9verser ?"], "Large file size warning": ["Avertissement de taille de fichier \u00e9lev\u00e9e"], "Server error: ": ["Erreur serveur :"], "The notebook list is empty.": ["La liste des notebooks est vide."], "Click here to rename, delete, etc.": ["Cliquer ici pour renommer, supprimer, etc."], "Running": ["Actif"], "Enter a new file name:": ["Saisir le nom du nouveau fichier :"], "Enter a new directory name:": ["Saisir le nom du nouveau r\u00e9pertoire :"], "Enter a new name:": ["Saisir un nouveau nom :"], "Rename file": ["Renommer le fichier"], "Rename directory": ["Renommer le r\u00e9pertoire"], "Rename notebook": ["Renommer le notebook"], "Move": ["D\u00e9placer"], "An error occurred while renaming \"%1$s\" to \"%2$s\".": ["Une erreur s'est produite pendant le renommage de \u00ab\u00a0%1$s\u00a0\u00bb vers \u00ab\u00a0%2$s\u00a0\u00bb."], "Rename Failed": ["\u00c9chec du Renommage"], "Enter a new destination directory path for this item:": ["Saisir un nouveau chemin de destination pour cet \u00e9l\u00e9ment :", "Saisir un nouveau chemin de destination pour ces %d \u00e9l\u00e9ments :"], "Move an Item": ["D\u00e9placer un \u00e9l\u00e9ment", "D\u00e9placer %d \u00e9l\u00e9ments"], "An error occurred while moving \"%1$s\" from \"%2$s\" to \"%3$s\".": ["Une erreur s'est produite lors du d\u00e9placement de \u00ab\u00a0%1$s\u00a0\u00bb de \u00ab\u00a0%2$s\u00a0\u00bb vers \u00ab\u00a0%3$s\u00a0\u00bb."], "Move Failed": ["\u00c9chec du d\u00e9placement"], "Are you sure you want to permanently delete: \"%s\"?": ["\u00cates-vous certain de vouloir supprimer d\u00e9finitivement \u00ab\u00a0%s\u00a0 \u00bb ?", "\u00cates-vous certain de vouloir supprimer d\u00e9finitivement les \u00ab\u00a0%d\u00a0 \u00bb fichiers ou r\u00e9pertoires s\u00e9lectionn\u00e9s ?"], "An error occurred while deleting \"%s\".": ["Une erreur s'est produite pendant la suppression de \u00ab %s \u00bb."], "Delete Failed": ["\u00c9chec de la suppression"], "Are you sure you want to duplicate: \"%s\"?": ["\u00cates-vous certain de vouloir dupliquer \u00ab\u00a0%s\u00a0\u00bb ?", "\u00cates-vous certain de vouloir dupliquer les \u00ab\u00a0%d\u00a0\u00bb fichiers s\u00e9lectionn\u00e9s ?"], "Duplicate": ["Dupliquer"], "An error occurred while duplicating \"%s\".": ["Une erreur s'est produite pendant la duplication de \u00ab\u00a0%s\u00a0\u00bb."], "Duplicate Failed": ["\u00c9chec de la duplication"], "Upload": ["T\u00e9l\u00e9verser"], "Invalid file name": ["Nom de fichier invalide"], "File names must be at least one character and not start with a period": ["Les noms des fichier doivent compter au moins un caract\u00e8re et ne doivent pas commencer avec un point."], "Cannot upload invalid Notebook": ["Impossible de t\u00e9l\u00e9verser un Notebook invalide"], "There is already a file named \"%s\". Do you want to replace it?": ["Il y a d\u00e9j\u00e0 un fichier nomm\u00e9 \u00ab\u00a0%s\u00a0\u00bb. Souhaitez-vous le remplacer ?"], "Replace file": ["Remplacer le fichier"]}}};
    document.documentElement.lang = navigator.language.toLowerCase();
    </script>

    
    

<script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="services/contents" src="gluton1_fichiers/contents.js"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="custom/custom" src="gluton1_fichiers/custom.js"></script></head>

<body class="" data-jupyter-api-token="cb8fa463e069eb01e89f336641ea9541ed557dab1d98e9c7" data-base-url="/" data-notebook-path="période 2" data-terminals-available="True" data-server-root="P:\nsi" dir="ltr">

<noscript>
    <div id='noscript'>
      Jupyter Notebook requires JavaScript.<br>
      Please enable it to proceed. 
  </div>
</noscript>

<div id="header" role="navigation" aria-label="Top Menu" style="display: block;">
  <div id="header-container" class="container">
  <div id="ipython_notebook" class="nav navbar-brand"><a href="http://localhost:8888/tree?token=cb8fa463e069eb01e89f336641ea9541ed557dab1d98e9c7" title="dashboard">
      <img src="gluton1_fichiers/logo.png" alt="Jupyter Notebook">
  </a></div>

  
  <span class="flex-spacer"></span>
  
  
  
    <span id="shutdown_widget">
      <button id="shutdown" class="btn btn-sm navbar-btn" title="Stop the Jupyter server">
          Quit
      </button>
    </span>
  

  
  
  
  

    <span id="login_widget">
      
        <button id="logout" class="btn btn-sm navbar-btn">Logout</button>
      
    </span>

  

  
  
  </div>
  <div class="header-bar"></div>

  
  
</div>

<div id="site" style="display: block; height: 1074.5px;">


  <div id="ipython-main-app" class="container">
    <div id="tab_content" class="tabbable" role="main">
      <ul id="tabs" class="nav nav-tabs">
        <li class="active"><a href="#notebooks" data-toggle="tab">Files</a></li>
        <li><a href="#running" data-toggle="tab">Running</a></li>
        <li><a href="#clusters" data-toggle="tab" class="clusters_tab_link">Clusters</a></li>
      </ul>
      <div class="tab-content">
        <div id="notebooks" class="tab-pane active">
          <div id="notebook_toolbar" class="row list_toolbar">
            <div class="col-sm-8 no-padding">
              <div class="dynamic-instructions" style="">
                Select items to perform actions on them.
              </div>
              <div class="dynamic-buttons">
                  <button title="Duplicate selected" aria-label="Duplicate" class="duplicate-button btn btn-default btn-xs" style="display: none;">Duplicate</button>
                  <button title="Rename selected" aria-label="Rename" class="rename-button btn btn-default btn-xs" style="display: none;">Rename</button>
                  <button title="Move selected" aria-label="Move" class="move-button btn btn-default btn-xs" style="display: none;">Move</button>
                  <button title="Download selected" aria-label="Download" class="download-button btn btn-default btn-xs" style="display: none;">Download</button>
                  <button title="Shutdown selected notebook(s)" aria-label="Shutdown" class="shutdown-button btn btn-default btn-xs btn-warning" style="display: none;">Shutdown</button>
                  <button title="View selected" aria-label="View" class="view-button btn btn-default btn-xs" style="display: none;">View</button>
                  <button title="Edit selected" aria-label="Edit" class="edit-button btn btn-default btn-xs" style="display: none;">Edit</button>
                  <button title="Delete selected" aria-label="Delete selected" class="delete-button btn btn-default btn-xs btn-danger" style="display: none;"><i class="fa fa-trash"></i></button>
              </div>
            </div>
            <div class="col-sm-4 no-padding tree-buttons">
              <div class="pull-right">
                <form id="alternate_upload" class="alternate_upload">
                  <span id="notebook_list_info" class="toolbar_info">
                  <span id="upload_span" class="btn btn-xs btn-default btn-upload" role="button" tabindex="0">
                    <input id="upload_span_input" title="Click to browse for a file to upload." type="file" name="datafile" class="fileinput" multiple="multiple" tabindex="-1">
                    Upload
                  </span>
                  </span>
                </form>
                <div id="new-buttons" class="btn-group">
                  <button class="dropdown-toggle btn btn-default btn-xs" id="new-dropdown-button" data-toggle="dropdown">
                  <span>New</span>
                  <span class="caret"></span>
                  <span class="sr-only">Toggle Dropdown</span>
                  </button>
                  <ul id="new-menu" class="dropdown-menu" role="menu">
                    <li role="menuitem" class="dropdown-header" id="notebook-kernels">Notebook:</li><li id="kernel-python3"><a aria-label="python3" role="menuitem" href="#" title="Créer un nouveau notebook avec Python 3">Python 3</a></li>
                    <li role="presentation" class="divider"></li>
                    <li role="menuitem" class="dropdown-header">Other:</li>
                    <li role="none" id="new-file">
                        <a role="menuitem" tabindex="-1" href="#">Text File</a>
                    </li>
                    <li role="none" id="new-folder">
                        <a role="menuitem" tabindex="-1" href="#">Folder</a>
                    </li>
                    
                    <li role="none" id="new-terminal">
                        <a role="menuitem" tabindex="-1" href="#">Terminal</a>
                    </li>
                    
                  </ul>
                </div>
                <div class="btn-group">
                    <button id="refresh_notebook_list" title="Refresh notebook list" aria-label="Refresh notebook list" class="btn btn-default btn-xs"><i class="fa fa-refresh"></i></button>
                </div>
              </div>
            </div>
          </div>
          <div id="notebook_list" class="list_container">
            <div id="notebook_list_header" class="row list_header">
              <div class="btn-group dropdown" id="tree-selector">
                <button title="Select All / None" aria-label="Select All/None" type="button" class="btn btn-default btn-xs" id="button-select-all" role="checkbox">
                  <input type="checkbox" class="pull-left tree-selector" id="select-all" tabindex="-1"><span id="counter-select-all">0</span>
                </button>
                <button title="Select Folders/All Notebooks/Running/Files" class="btn btn-default btn-xs dropdown-toggle" type="button" id="tree-selector-btn" data-toggle="dropdown" aria-expanded="true">
                  <span class="sr-only">checkbox</span>
                  <span class="caret"></span>
                  <span class="sr-only">Toggle Dropdown</span>
                </button>
                <ul id="selector-menu" class="dropdown-menu" role="menu" aria-labelledby="tree-selector-btn">
                  <li role="none"><a id="select-folders" role="menuitem" tabindex="-1" href="#" title="Select All Folders"><i class="menu_icon folder_icon icon-fixed-width"></i>&nbsp;Folders</a></li>
                  <li role="none"><a id="select-notebooks" role="menuitem" tabindex="-1" href="#" title="Select All Notebooks"><i class="menu_icon notebook_icon icon-fixed-width"></i>&nbsp;All Notebooks</a></li>
                  <li role="none"><a id="select-running-notebooks" role="menuitem" tabindex="-1" href="#" title="Select Running Notebooks"><i class="menu_icon running_notebook_icon icon-fixed-width"></i>&nbsp;Running</a></li>
                  <li role="none"><a id="select-files" role="menuitem" tabindex="-1" href="#" title="Select All Files"><i class="menu_icon file_icon icon-fixed-width"></i>&nbsp;Files</a></li>
                </ul>
              </div>
              <div id="project_name">
                <ul class="breadcrumb"><li><a href="http://localhost:8888/tree" title="Link to root folder"><i class="fa fa-folder"></i></a></li><li><a href="http://localhost:8888/tree/p%C3%A9riode%202">période 2</a></li></ul>
              </div>
              <div id="sort_buttons" class="pull-right">
                <div id="sort_name" class="sort_button">
                  <button type="button" class="btn btn-xs btn-default sort-action" id="sort-name" aria-label="Sort by name">
                        Name
                        <i class="fa fa-arrow-down"></i>
                  </button>
                </div>
                <div id="last_modified" class="sort_button">
                    <button type="button" class="btn btn-xs btn-default sort-action" id="last-modified" aria-label="Sort by last modified">
                        Last Modified
                        <i class="fa"></i>
                    </button>
                </div>
                <div id="file_size" class="sort_button">
                    <button type="button" class="btn btn-xs btn-default sort-action" id="file-size" aria-label="Sort by file size">
                        File size
                        <i class="fa"></i>
                    </button>
                </div>
              </div>
            </div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Cliquer ici pour renommer, supprimer, etc." style="visibility: hidden;"><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree"><span class="item_name">..</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Actif</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-04-12 16:59">il y a quelques secondes</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Cliquer ici pour renommer, supprimer, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/p%C3%A9riode%202/tp4_reseau_files"><span class="item_name">tp4_reseau_files</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Actif</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-03-10 09:31">il y a un mois</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Cliquer ici pour renommer, supprimer, etc."><i class="item_icon running_notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/p%C3%A9riode%202/Algorithme%20Glouton.ipynb" target="_blank"><span class="item_name">Algorithme Glouton.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="">Actif</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-04-12 16:58">il y a 2 minutes</span><span class="file_size pull-right">10.2 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Cliquer ici pour renommer, supprimer, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/p%C3%A9riode%202/bibliotheque.py" target="_blank"><span class="item_name">bibliotheque.py</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Actif</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-01-06 10:10">il y a 3 mois</span><span class="file_size pull-right">1.69 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Cliquer ici pour renommer, supprimer, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/p%C3%A9riode%202/code.txt" target="_blank"><span class="item_name">code.txt</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Actif</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-03-29 17:01">il y a 14 jours</span><span class="file_size pull-right">363 B</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Cliquer ici pour renommer, supprimer, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/p%C3%A9riode%202/codebis.txt" target="_blank"><span class="item_name">codebis.txt</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Actif</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-03-31 10:10">il y a 12 jours</span><span class="file_size pull-right">1.53 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Cliquer ici pour renommer, supprimer, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/p%C3%A9riode%202/coder%20en%20binaire.py" target="_blank"><span class="item_name">coder en binaire.py</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Actif</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-11-25 10:04">il y a 5 mois</span><span class="file_size pull-right">223 B</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Cliquer ici pour renommer, supprimer, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/p%C3%A9riode%202/correction_turtle.py" target="_blank"><span class="item_name">correction_turtle.py</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Actif</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-01-20 09:48">il y a 3 mois</span><span class="file_size pull-right">1 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Cliquer ici pour renommer, supprimer, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/p%C3%A9riode%202/devoir_cassv.py" target="_blank"><span class="item_name">devoir_cassv.py</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Actif</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-01-20 09:06">il y a 3 mois</span><span class="file_size pull-right">1.37 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Cliquer ici pour renommer, supprimer, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/p%C3%A9riode%202/exercic_jeudi_1_dec.py" target="_blank"><span class="item_name">exercic_jeudi_1_dec.py</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Actif</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-12-07 16:06">il y a 4 mois</span><span class="file_size pull-right">200 B</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Cliquer ici pour renommer, supprimer, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/p%C3%A9riode%202/exercice2.py" target="_blank"><span class="item_name">exercice2.py</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Actif</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-12-07 16:06">il y a 4 mois</span><span class="file_size pull-right">634 B</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Cliquer ici pour renommer, supprimer, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/p%C3%A9riode%202/exo_dico.py" target="_blank"><span class="item_name">exo_dico.py</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Actif</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-12-02 08:37">il y a 4 mois</span><span class="file_size pull-right">1.41 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Cliquer ici pour renommer, supprimer, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/p%C3%A9riode%202/exo_dico_suite.py" target="_blank"><span class="item_name">exo_dico_suite.py</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Actif</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-12-02 09:31">il y a 4 mois</span><span class="file_size pull-right">2.36 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Cliquer ici pour renommer, supprimer, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/p%C3%A9riode%202/fichier.csv" target="_blank"><span class="item_name">fichier.csv</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Actif</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-02-01 16:33">il y a 2 mois</span><span class="file_size pull-right">12.8 MB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Cliquer ici pour renommer, supprimer, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/p%C3%A9riode%202/gluton.py" target="_blank"><span class="item_name">gluton.py</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Actif</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-04-12 16:52">il y a 7 minutes</span><span class="file_size pull-right">3.93 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Cliquer ici pour renommer, supprimer, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/view/p%C3%A9riode%202/graphique1.png" target="_blank"><span class="item_name">graphique1.png</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Actif</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-01-06 10:08">il y a 3 mois</span><span class="file_size pull-right">18.7 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Cliquer ici pour renommer, supprimer, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/p%C3%A9riode%202/ile_de_france.py" target="_blank"><span class="item_name">ile_de_france.py</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Actif</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-02-01 16:59">il y a 2 mois</span><span class="file_size pull-right">1.37 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Cliquer ici pour renommer, supprimer, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/p%C3%A9riode%202/reseau.pkt" target="_blank"><span class="item_name">reseau.pkt</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Actif</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-02-10 10:11">il y a 2 mois</span><span class="file_size pull-right">7.5 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Cliquer ici pour renommer, supprimer, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/view/p%C3%A9riode%202/tp4_reseau.html" target="_blank"><span class="item_name">tp4_reseau.html</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Actif</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-02-17 09:53">il y a 2 mois</span><span class="file_size pull-right">1.1 MB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Cliquer ici pour renommer, supprimer, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/p%C3%A9riode%202/travail_supp.py" target="_blank"><span class="item_name">travail_supp.py</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Actif</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-01-11 17:03">il y a 3 mois</span><span class="file_size pull-right">759 B</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Cliquer ici pour renommer, supprimer, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/p%C3%A9riode%202/tuple.py" target="_blank"><span class="item_name">tuple.py</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Actif</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-12-02 08:36">il y a 4 mois</span><span class="file_size pull-right">1.14 kB</span></div></div></div></div>
          </div>
        </div>
        <div id="running" class="tab-pane">
          <div id="running_toolbar" class="row list_toolbar">
            <div class="col-sm-8 no-padding">
              <span id="running_list_info" class="toolbar_info">Currently running Jupyter processes</span>
            </div>
            <div class="col-sm-4 no-padding tree-buttons">
              <span id="running_buttons" class="pull-right toolbar_buttons">
              <button id="refresh_running_list" title="Refresh running list" aria-label="Refresh running list" class="btn btn-default btn-xs"><i class="fa fa-refresh"></i></button>
              </span>
            </div>
          </div>
          <div class="panel-group" id="accordion">
            <div class="panel panel-default">
              <div class="panel-heading">
                <a data-toggle="collapse" data-target="#collapseOne" href="#">
                  Terminals
                <i class="fa fa-caret-down"></i></a>
              </div>
              <div id="collapseOne" class=" collapse in">
                <div class="panel-body">
                  <div id="terminal_list" class="list_container">
                    <div id="terminal_list_header" class="row list_placeholder">
                    
                      <div> There are no terminals running. </div>
                    
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="panel panel-default">
              <div class="panel-heading">
                <a data-toggle="collapse" data-target="#collapseTwo" href="#">
                  Notebooks
                <i class="fa fa-caret-down"></i></a>
              </div>
              <div id="collapseTwo" class=" collapse in">
                <div class="panel-body">
                  <div id="running_list" class="list_container">
                    <div id="running_list_placeholder" class="row list_placeholder" style="display: none;">
                      <div> There are no notebooks running. </div>
                    </div>
                  <div class="list_item row"><div class="col-md-12"><i class="item_icon running_notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/p%C3%A9riode%202/Algorithme%20Glouton.ipynb" target="_blank"><span class="item_name">période 2/Algorithme Glouton.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="kernel-name">Python 3</div><button class="btn btn-warning btn-xs">Arrêter</button></div><div class="pull-right"><span class="item_modified pull-left" title="2022-04-12 17:00">il y a quelques secondes</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div id="clusters" class="tab-pane">
          Clusters tab is now provided by IPython parallel.
          See '<a href="https://github.com/ipython/ipyparallel">IPython parallel</a>' for installation details.
        </div>
      </div><!-- class:tab-content -->
    </div><!-- id:tab_content -->
  </div><!-- ipython-main-app  -->


</div>





    



<script src="gluton1_fichiers/main.js" type="text/javascript" charset="utf-8"></script>


<script type="text/javascript">
  function _remove_token_from_url() {
    if (window.location.search.length <= 1) {
      return;
    }
    var search_parameters = window.location.search.slice(1).split('&');
    for (var i = 0; i < search_parameters.length; i++) {
      if (search_parameters[i].split('=')[0] === 'token') {
        // remote token from search parameters
        search_parameters.splice(i, 1);
        var new_search = '';
        if (search_parameters.length) {
          new_search = '?' + search_parameters.join('&');
        }
        var new_url = window.location.origin + 
                      window.location.pathname + 
                      new_search + 
                      window.location.hash;
        window.history.replaceState({}, "", new_url);
        return;
      }
    }
  }
  _remove_token_from_url();
</script>


</body></html>