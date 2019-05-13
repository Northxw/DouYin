function c(t, b, k) {
    function u(e) {
        v[x++] = e
    }
    function f() {
        return g = t.charCodeAt(b++) - 32,
        t.substring(b, b += g)
    }
    function l() {
        try {
            y = c(t, b, k)
        } catch(e) {
            h = e,
            y = l
        }
    }
    for (var h, y, d, g, v = [], x = 0;;) switch (g = t.charCodeAt(b++) - 32) {
    case 1:
        u(!v[--x]);
        break;
    case 4:
        v[x++] = f();
        break;
    case 5:
        u(function(e) {
            var a = 0,
            r = e.length;
            return function() {
                var c = a < r;
                return c && u(e[a++]),
                c
            }
        } (v[--x]));
        break;
    case 6:
        y = v[--x],
        u(v[--x](y));
        break;
    case 8:
        if (g = t.charCodeAt(b++) - 32, l(), b += g, g = t.charCodeAt(b++) - 32, y === c) b += g;
        else if (y !== l) return y;
        break;
    case 9:
        v[x++] = c;
        break;
    case 10:
        u(s(v[--x]));
        break;
    case 11:
        y = v[--x],
        u(v[--x] + y);
        break;
    case 12:
        for (y = f(), d = [], g = 0; g < y.length; g++) d[g] = y.charCodeAt(g) ^ g + y.length;
        u(String.fromCharCode.apply(null, d));
        break;
    case 13:
        y = v[--x],
        h = delete v[--x][y];
        break;
    case 14:
        v[x++] = t.charCodeAt(b++) - 32;
        break;
    case 59:
        u((g = t.charCodeAt(b++) - 32) ? (y = x, v.slice(x -= g, y)) : []);
        break;
    case 61:
        u(v[--x][t.charCodeAt(b++) - 32]);
        break;
    case 62:
        g = v[--x],
        k[0] = 65599 * k[0] + k[1].charCodeAt(g) >>> 0;
        break;
    case 65:
        h = v[--x],
        y = v[--x],
        v[--x][y] = h;
        break;
    case 66:
        u(e(t[b++], v[--x], v[--x]));
        break;
    case 67:
        y = v[--x],
        d = v[--x],
        u((g = v[--x]).x === c ? r(g.y, y, k) : g.apply(d, y));
        break;
    case 68:
        u(e((g = t[b++]) < "<" ? (b--, f()) : g + g, v[--x], v[--x]));
        break;
    case 70:
        u(!1);
        break;
    case 71:
        v[x++] = n;
        break;
    case 72:
        v[x++] = +f();
        break;
    case 73:
        u(parseInt(f(), 36));
        break;
    case 75:
        if (v[--x]) {
            b++;
            break
        }
    case 74:
        g = t.charCodeAt(b++) - 32 << 16 >> 16,
        b += g;
        break;
    case 76:
        u(k[t.charCodeAt(b++) - 32]);
        break;
    case 77:
        y = v[--x],
        u(v[--x][y]);
        break;
    case 78:
        g = t.charCodeAt(b++) - 32,
        u(a(v, x -= g + 1, g));
        break;
    case 79:
        g = t.charCodeAt(b++) - 32,
        u(k["$" + g]);
        break;
    case 81:
        h = v[--x],
        v[--x][f()] = h;
        break;
    case 82:
        u(v[--x][f()]);
        break;
    case 83:
        h = v[--x],
        k[t.charCodeAt(b++) - 32] = h;
        break;
    case 84:
        v[x++] = !0;
        break;
    case 85:
        v[x++] = void 0;
        break;
    case 86:
        u(v[x - 1]);
        break;
    case 88:
        h = v[--x],
        y = v[--x],
        v[x++] = h,
        v[x++] = y;
        break;
    case 89:
        u(function() {
            function e() {
                return r(e.y, arguments, k)
            }
            return e.y = f(),
            e.x = c,
            e
        } ());
        break;
    case 90:
        v[x++] = null;
        break;
    case 91:
        v[x++] = h;
        break;
    case 93:
        h = v[--x];
        break;
    case 0:
        return v[--x];
    default:
        u((g << 16 >> 16) - 16)
    }
}