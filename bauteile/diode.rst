.. index:: Diode
.. _Diode:
.. _Dioden:

Dioden
======

Ähnlich wie eine :ref:`Röhrendiode <Röhrendiode>` stellt eine Halbleiter-Diode
eine "elektrische Einbahnstraße" dar; elektrischer Strom kann eine
Halbleiter-Diode in nur einer Richtung passieren.

.. _Normale Diode:

"Normale" Dioden
----------------

Eine Diode verfügt über zwei Anschlüsse, die als Anode und Kathode bezeichnet
werden. Strom kann nur durch eine Diode fließen, wenn die Anode zum Plus- und
die Kathode zum Minus-Pol zeigt; in der Gegenrichtung sperrt sie. Auf dem
Bauteil ist die Kathoden-Seite durch ein schwarzen oder weißen Ring
gekennzeichnet. Ab einer anliegenden Spannungsdifferenz von etwa
:math:`U_{\mathrm{D}} = \unit[0,7]{V}` beginnt in Durchlassrichtung Strom zu
fließen.

.. figure::
    ../pics/bauteile/schaltzeichen-diode.png
    :name: fig-schaltzeichen-diode
    :alt:  fig-schaltzeichen-diode
    :align: center
    :width: 30%

    Schaltzeichen einer Diode. Der linke Anschlussdraht wird Anode, der rechte
    Kathode genannt.

    .. only:: html

        :download:`SVG: Schaltzeichen Diode
        <../pics/bauteile/schaltzeichen-diode.svg>`

Beim Durchgang durch eine Diode sinkt die Spannung -- anders als bei Ohmschen
Widerständen, die zum Durchlassen einer größeren Stromstärke stets auch eine
größere anliegende elektrische Spannung benötigen -- relativ konstant um
:math:`\unit[0,7]{V}` -- weitgehend unabhängig von der Stärke des fließenden
Stroms. Das Ohmsche Gesetz :math:`U = R \cdot I` ist somit nicht auf Dioden
anwendbar.

.. figure::
    ../pics/bauteile/kennlinie-diode-durchlassrichtung.png
    :name: fig-kennlinie-diode-durchlassrichtung
    :alt:  fig-kennlinie-diode-durchlassrichtung
    :align: center
    :width: 50%

    Kennlinie einer Diode in Durchlassrichtung.

    .. only:: html

        :download:`SVG: Kennlinie einer Diode in Durchlassrichtung.
        <../pics/bauteile/kennlinie-diode-durchlassrichtung.svg>`

Legt man eine entgegengesetzte Spannung :math:`U_{\mathrm{S}}` an, so verhält sich
eine Diode bis zu einem bestimmten Spannungswert wie ein Isolator -- die Diode
"sperrt". Wird der Spannungswert, der vom Bautyp und Material der Diode abhängt,
überschritten, so nimmt die (ebenfalls in Gegenrichtung) fließende Stromstärke
:math:`I_{\mathrm{S}}` rasant zu; die Diode kann dabei schnell überhitzt bzw.
zerstört werden.

.. figure::
    ../pics/bauteile/kennlinie-diode-sperrrichtung.png
    :name: fig-kennlinie-diode-sperrichtung
    :alt:  fig-kennlinie-diode-sperrichtung
    :align: center
    :width: 50%

    Kennlinie einer :math:`\unit[100]{V}`-Diode in Sperrichtung.

    .. only:: html

        :download:`SVG: Kennlinie einer 100-V-Diode in Sperrichtung.
        <../pics/bauteile/kennlinie-diode-sperrrichtung.svg>`

Auf jeder Diode sind daher zwei charakteristische Werte aufgedruckt:

* Die in Volt angegebene Spannung sagt aus, mit welcher Spannung die Diode
  maximal entgegen der Durchlassrichtung (in "Sperrichtung") betrieben werden
  darf.

* Die in (Milli-)Ampere angegebene Stromstärke gibt an, welcher Strom maximal
  durch die Diode fließen darf.

Beide Werte dürfen nicht überschritten werden, da die Diode ansonsten zerstört
werden kann.

*Beispiel:*

* Für die Diode ``1N4001`` sind die Werte :math:`\unit[50]{V}/\unit[1]{A}`
  angegeben -- die maximale Spannung in Sperrichtung darf somit höchstens
  :math:`\unit[50]{V}`, die maximale Stromstärke in Durchlassrichtung
  höchstens :math:`\unit[1]{A}` betragen.


.. index::
    single: Diode; Leuchtdiode (LED)
    single: Leuchtdiode (LED)
.. _Leuchtdiode:

Leuchtdioden
------------

Leuchtdioden ("Light Emitting Diods", kurz: LEDs) sind spezielle Dioden, die in
einem durchsichtigen Gehäuse eingebaut sind und aufleuchten, wenn Strom durch
sie fließt. Die übliche Betriebspannung einer Leuchtdiode liegt normalerweise
bei :math:`U = \unit[1,4]{V}`; maximal darf an LEDs (je nach Bautyp) eine
Spannung von :math:`\unit[1,6]{V} \le U_{\mathrm{max}} \le \unit[2,4]{V}` angelegt
werden. [#]_ Die Stromstärke :math:`I` beträgt dabei zwischen
:math:`\unit[15]{mA}` und :math:`\unit[25]{mA}`.

.. figure::
    ../pics/bauteile/schaltzeichen-diode-leuchtdiode.png
    :name: fig-schaltzeichen-leuchtdiode
    :alt:  fig-schaltzeichen-leuchtdiode
    :align: center
    :width: 30%

    Schaltzeichen einer Leuchtdiode (LED).

    .. only:: html

        :download:`SVG: Schaltzeichen Leuchtdiode
        <../pics/bauteile/schaltzeichen-diode-leuchtdiode.svg>`

Die Anode der Leuchtdiode, die durch einen längeren Anschlussdraht
gekennzeichnet ist, muss mit dem Pluspol und die Kathode  mit dem Minuspol der
Stromquelle verbunden sein. Die Anoden- und Kathodenseite einer LED lässt sich,
wie in Abbildung :ref:`Bauform Leuchtdiode <fig-bauform-Leuchtdiode>`
dargestellt, ebenfalls anhand ihres Innenaufbaus erkennen.

.. figure::
    ../pics/bauteile/bauform-leuchtdiode.png
    :name: fig-bauform-leuchtdiode
    :alt:  fig-bauform-leuchtdiode
    :align: center
    :width: 40%

    Bauform einer Leuchtdiode (LED).

    .. only:: html

        :download:`SVG: Bauform einer Leuchtdiode
        <../pics/bauteile/bauform-leuchtdiode.svg>`

Leuchtdioden haben eine Vielzahl an wichtigen Eigenschaften: Sie benötigen nur
eine geringe Betriebspannung, sie unempfindlich gegen Stöße, benötigen nur wenig
Platz und haben einen nur geringen Strombedarf. Zudem haben Leuchtdioden sehr
schnelle Reaktionszeit: Sie können in einer Sekunde tausende Male ein- und
wieder ausgeschaltet werden und daher, ähnlich wie früher die "Morse-Tasten",
bei einer geeigneten Codierung zur Signalübertragung verwendet werden.

.. index::
    single: Diode; Photodiode
    single: Photodiode

.. _Photodiode:

Photodioden
-----------

Trifft Licht auf eine Photodiode, so wird in dieser ein elektrischer Strom
ausgelöst, der als Photostrom :math:`I_{\mathrm{P}}` bezeichnet wird. Je nach
Ausführung liegt die Lichtempfindlichkeit der Photodiode im Infrarot-,
Ultraviolett- oder im sichtbaren Bereich des Lichts.

.. figure::
    ../pics/bauteile/schaltzeichen-diode-fotodiode.png
    :name: fig-schaltzeichen-fotodiode
    :alt:  fig-schaltzeichen-fotodiode
    :align: center
    :width: 30%

    Schaltzeichen einer Fotodiode.

    .. only:: html

        :download:`SVG: Schaltzeichen Fotodiode
        <../pics/bauteile/schaltzeichen-diode-fotodiode.svg>`



.. _Solarzelle:

.. rubric:: Solarzellen

Eine Solarzelle besteht im Prinzip ebenfalls aus einer großflächigen Photodiode.
Häufig bestehen Solarzellen aus dünnen Silicium-Scheiben, die auf der
Vorderseite :math:`p`-dotiert und auf der Rückseite :math:`n`-dotiert sind.
Beide Seiten sind dabei mit gitter-artigen elektrischen Kontakten versehen.

Gelangt Licht durch die sehr dünne :math:`n`-dotierte Schicht hindurch auf die
:math:`p`-dotierte Schicht, so werden dort Elektronen aus ihren Bindungen
heraus gelöst; es werden also Elektronen-Loch-Paare erzeugt. In der
:math:`n`-dotierten Schicht sammelt sich dadurch ein Überangebot an Elektronen
an. Diese Elektronen werden allerdings durch die Sperrschicht der Diode daran
gehindert, unmittelbar wieder für einen Ladungsausgleich zu sorgen. Die
Elektronen fließen vielmehr durch den äußeren Stromkreis zur :math:`p`-dotierten
Schicht zurück.

Wird eine Solarzelle beleuchtet, dann liegt an ihren Polen eine Spannung von ca.
:math:`\unit[0,6]{V}` an ("Leerlaufspannung"). Diese Spannung sinkt ab, wenn ein
Verbraucher angeschlossen wird.

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkung:

.. [#]  Die zulässigen Spannungen von Leuchtdioden sind je nach
    Helligkeit und Farbe unterschiedlich; hierbei sind die Herstellerangaben zu
    beachten. Typischerweise liegt die Betriebsspannung bei roten LEDs bei
    :math:`\unit[1,9]{V}`, bei gelben LEDs bei :math:`\unit[2,0]{V}`, bei
    grünen LEDs bei :math:`\unit[2,4]{V}`. Blaue und weiße LEDs werden
    teilweise sogar mit :math:`3 \text{ bis } \unit[3,5]{V}` betrieben. Die
    Stromstärke liegt jeweils bei :math:`\unit[20]{mA}`.

